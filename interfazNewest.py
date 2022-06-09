from cmath import log
import sqlite3
import sys
from pathlib import Path
from PySide6 import QtCore
from PySide6.QtCore import QAbstractListModel, Qt, QUrl
from PySide6.QtSql import *
from PySide6.QtWidgets import *
from PySide6.QtGui import QColor
from newest import Ui_MainWindow
import scrapPeliculas
import scrapSeries
import scrapLibros
import scrapVideojuegos
import Crud
from pantallaDeCarga import Ui_VentanaDeCarga
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import logging
import constantes
import socket
import threading as th


counter = 0


class ventanaDeCarga(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaDeCarga()
        self.ui.setupUi(self)

        if not self.hayInternet():
            self.ui.mensajeNoInternet.exec()
            sys.exit()
        else:
            # Eliminamos la barra de titulo
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            # Sombra
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 60))
            self.ui.contenedor.setGraphicsEffect(self.shadow)

            # Timer
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)
            # Tiempo en milisegundos
            self.timer.start(5)

            # Cambiamos el valor del label dependiendo del tiempo de carga
            # Texto inicial
            self.ui.labelDescripcion.setText(constantes.CARGA_BIENVENIDO)
            # Cambio de texto
            QtCore.QTimer.singleShot(
                500, lambda: self.ui.labelDescripcion.setText(constantes.CARGA_BIBLIOTECA))
            QtCore.QTimer.singleShot(
                1000, lambda: self.ui.labelDescripcion.setText(constantes.CARGA_PELICULAS))
            QtCore.QTimer.singleShot(
                1500, lambda: self.ui.labelDescripcion.setText(constantes.CARGA_SERIES))
            QtCore.QTimer.singleShot(
                2000, lambda: self.ui.labelDescripcion.setText(constantes.CARGA_LIBROS))
            QtCore.QTimer.singleShot(
                2500, lambda: self.ui.labelDescripcion.setText(constantes.CARGA_VIDEOJUEGOS))
            QtCore.QTimer.singleShot(
                3000, lambda: self.ui.labelDescripcion.setText(constantes.CARGA_ESPERE))
            QtCore.QTimer.singleShot(3500, lambda: self.ui.labelCargando.setText(
                constantes.MEJORANDO_EXPERIENCIA))

            self.show()

    def progress(self):
        '''
        Manejamos la barra de progreso estableciendo su valor
        y lanzando la ventana principal cuando termina la carga
        '''
        global counter

        self.ui.progressBar.setValue(counter)

        # Cerramos la ventana de carga y abrimos MainWIndow
        if counter >= 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.showMaximized()
            self.close()
        counter += 1

    
    def hayInternet(self):
        '''
        return : Si hay internet en el equipo
        '''
        miSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        miSocket.settimeout(5)
        try:
            miSocket.connect(("www.google.com", 80))
            miSocket.close()
        except (socket.gaierror, socket.timeout):
            miSocket.close()
            return False
        else:
            miSocket.close()
            return True


class TaskModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.array = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.array[index.row()]

    def rowCount(self, index):
        return len(self.array)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        app.setStyle("Fusion")
        app.setStyleSheet('background-color: black;')
        self.setupUi(self)
        self.setMinimumSize(QtCore.QSize(800, 800))

        # Establecemos un contador para cuando carguemos los datos de la BDD
        self.contPeliculas = 0
        self.contSeries = 0
        self.contLibros = 0
        self.contVideojuegos = 0

        # Creamos los modelos
        self.modelLibro = TaskModel()
        self.modelPelicula = TaskModel()
        self.modelSerie = TaskModel()
        self.modelVideojuego = TaskModel()

        # Obtenemos los item seleccionados en las listas
        self.indicePelicula = self.listView.currentIndex().row()
        self.indiceSerie = self.listView_2.currentIndex().row()
        self.indiceLibro = self.listView_3.currentIndex().row()
        self.indiceVideojuego = self.listView_4.currentIndex().row()

        # Lanzamos un arreglo de hilos que ejecutan el WebScrapping
        threadUno = th.Thread(target=self.establecerPeliculasRaspado)
        threadDos = th.Thread(target=self.establecerSeriesRaspado)
        threadTres = th.Thread(target=self.establecerLibrosRaspado)
        threadCuatro = th.Thread(target=self.establecerVideojuegosRaspado)

        threads = [threadUno, threadDos, threadTres, threadCuatro]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        # Establecemos el modelo de las tablas y de las listas
        self.establecerModelosTablas()
        self.establecerModeloListas()

        # Recargamos las tablas de la App con los datos de la BDD
        self.recargarSeries()
        self.recargarPeliculas()
        self.recargarLibros()
        self.recargarVideojuegos()

        # Añadimos las películas a los respectivos listView
        self.aniadirPeliculasListView()
        self.aniadirSeriesListView()
        self.aniadirLibrosListView()
        self.aniadirVideojuegosListView()

        # Cargamos el PDF con el manual de uso de la aplicación en la pestaña ayuda
        self.cargarPDFAyuda()

        # Enlazamos las acciones del menú
        self.actionHome.triggered.connect(self.cambiar_A_Inicio)
        self.actionPeliculas.triggered.connect(self.cambiar_A_Peliculas)
        self.actionSeries.triggered.connect(self.cambiar_A_Series)
        self.actionLibros.triggered.connect(self.cambiar_A_Libros)
        self.actionVideojuegos.triggered.connect(self.cambiar_A_Videojuegos)
        self.actionMi_biblioteca.triggered.connect(self.cambiar_A_Biblioteca)
        self.actionAyuda.triggered.connect(self.cambiar_A_Ayuda)

        # Enlazamos las acciones de los botones y del comboBox de la Biblioteca
        self.botonAniadirPelicula.clicked.connect(self.insertPelicula)
        self.botonAniadirSerie.clicked.connect(self.insertSerie)
        self.botonAniadirLibro.clicked.connect(self.insertLibro)
        self.botonAniadirVideojuego.clicked.connect(self.insertVideojuego)
        self.botonEliminarBiblioteca.clicked.connect(self.eliminar)
        self.comboTablas.currentTextChanged.connect(self.tabla_A_Mostrar)

    def establecerPeliculasRaspado(self):
        self.peliculas = scrapPeliculas.obtenerListaPeliculas()

    def establecerSeriesRaspado(self):
        self.series = scrapSeries.obtenerListaSeries()

    def establecerLibrosRaspado(self):
        self.libros = scrapLibros.obtenerListaLibros()

    def establecerVideojuegosRaspado(self):
        self.videojuegos = scrapVideojuegos.obtenerListaVideojuegos()

    def establecerModeloListas(self):
        self.listView.setModel(self.modelPelicula)
        self.listView_2.setModel(self.modelSerie)
        self.listView_3.setModel(self.modelLibro)
        self.listView_4.setModel(self.modelVideojuego)

    def establecerCuadrosDialogo(self):
        '''
        Configuración de los cuadros de diálogo de la App
        '''
        self.mensajeNoInternet = QMessageBox()
        self.mensajeNoInternet.setObjectName(u"mensajeNoInternet")
        self.mensajeNoInternet.setText("No hay internet")
        self.mensajeNoInternet.setIcon(QMessageBox.Critical)
        self.mensajeNoInternet.setText('Error en la conexion a internet')
        self.mensajeNoInternet.setInformativeText(
            'Intentelo de nuevo más tarde o pongase en contacto con su proveedor de Internet')
        self.mensajeNoInternet.setWindowTitle('ERROR')
        self.mensajeNoInternet.setStandardButtons(QMessageBox.Ok)

        self.infoItemAñadido = QMessageBox()
        self.infoItemAñadido .setIcon(QMessageBox.Information)
        self.infoItemAñadido .setWindowTitle('Añadida')
        self.infoItemAñadido .setStandardButtons(QMessageBox.Ok)
        self.infoItemAñadido .setDefaultButton(QMessageBox.Ok)

        self.infoItemYaAñadido = QMessageBox()
        self.infoItemYaAñadido.setIcon(QMessageBox.Information)
        self.infoItemYaAñadido.setWindowTitle('Ups')
        self.infoItemYaAñadido.setStandardButtons(QMessageBox.Ok)
        self.infoItemYaAñadido.setDefaultButton(QMessageBox.Ok)

    def insertPelicula(self):
        '''
        Recoge la pelicula seleccionada del listView de películas y la inserta en la BDD y en la tabla
        '''
        pelicula = self.peliculas[self.listView.currentIndex().row()]

        insertado = Crud.insertarPelicula(
            self.peliculas, self.listView.currentIndex().row())

        self.contPeliculas += 1

        if(insertado):
            self.tablePeliculas.insertRow(self.contPeliculas)
            self.tablePeliculas.setRowCount(self.contPeliculas)
            self.tablePeliculas.setItem(
                self.contPeliculas-1, 0, QTableWidgetItem(pelicula[0]))
            self.tablePeliculas.setItem(
                self.contPeliculas-1, 1, QTableWidgetItem(pelicula[1]))
            self.tablePeliculas.setItem(
                self.contPeliculas-1, 2, QTableWidgetItem(pelicula[2]))
            self.tablePeliculas.setItem(
                self.contPeliculas-1, 3, QTableWidgetItem(pelicula[3]))
            self.tablePeliculas.setItem(
                self.contPeliculas-1, 4, QTableWidgetItem(pelicula[4]))
            self.tablePeliculas.resizeColumnsToContents()
            self.infoItemAñadido.setText(
                f"Se ha añadido la película {pelicula[0]}")
            self.infoItemAñadido.exec()
            logging.info(f"Se ha añadido la película {pelicula[0]}")
        else:
            self.infoItemYaAñadido.setText(
                f"La película {pelicula[0]} ya se encuentra en Mi Biblioteca")
            self.infoItemYaAñadido.exec()
            logging.info(
                f"La película {pelicula[0]} ya se encuentra en Mi Biblioteca")
        self.recargarPeliculas()

    def insertSerie(self):
        '''
        Recoge la serie seleccionada del listView de series y la inserta en la BDD y en la tabla
        '''
        serie = self.series[self.listView_2.currentIndex().row()]
        insertado = Crud.insertarSerie(
            self.series, self.listView_2.currentIndex().row())

        self.contSeries += 1
        if(insertado):
            self.tableSeries.insertRow(self.contPeliculas)
            self.tableSeries.setRowCount(self.contPeliculas)

            self.tableSeries.setItem(
                self.contSeries-1, 0, QTableWidgetItem(serie[0]))
            self.tableSeries.setItem(
                self.contSeries-1, 1, QTableWidgetItem(serie[1]))
            self.tableSeries.setItem(
                self.contSeries-1, 2, QTableWidgetItem(serie[2]))
            self.tableSeries.setItem(
                self.contSeries-1, 3, QTableWidgetItem(serie[3]))
            self.tableSeries.setItem(
                self.contSeries-1, 4, QTableWidgetItem(serie[4]))
            self.tableSeries.resizeColumnsToContents()

            self.infoItemAñadido.setText(f"Se ha añadido la serie {serie[0]}")
            self.infoItemAñadido.exec()
            logging.info(f"Se ha añadido la serie {serie[0]}")
        else:
            self.infoItemYaAñadido.setText(
                f"La serie {serie[0]} ya se encuentra en Mi Biblioteca.")
            self.infoItemYaAñadido.exec()
            logging.info(
                f"La serie {serie[0]} ya se encuentra en Mi Biblioteca.")
        self.recargarSeries()

    def insertLibro(self):
        '''
        Recoge el libro seleccionado del listView de libros y lo inserta en la BDD y en la tabla
        '''
        libro = self.libros[self.listView_3.currentIndex().row()]
        insertado = Crud.insertarLibro(
            self.libros, self.listView_3.currentIndex().row())
        self.contLibros += 1

        if(insertado):
            self.tableLibros.insertRow(self.contLibros)
            self.tableLibros.setRowCount(self.contLibros)
            self.tableLibros.setItem(
                self.contLibros-1, 0, QTableWidgetItem(libro[0]))
            self.tableLibros.setItem(
                self.contLibros-1, 1, QTableWidgetItem(libro[1]))
            self.tableLibros.setItem(
                self.contLibros-1, 2, QTableWidgetItem(libro[2]))
            self.tableLibros.setItem(
                self.contLibros-1, 3, QTableWidgetItem(libro[3]))
            self.tableLibros.setItem(
                self.contLibros-1, 4, QTableWidgetItem(libro[4]))
            self.infoItemAñadido.setText(f"Se ha añadido el libro {libro[0]}")
            self.infoItemAñadido.exec()
            logging.info(f"Se ha añadido el libro {libro[0]}")
        else:
            self.infoItemYaAñadido.setText(
                f"El libro {libro[0]} ya se encuentra en Mi Biblioteca.")
            self.infoItemYaAñadido.exec()
            logging.info(
                f"El libro {libro[0]} ya se encuentra en Mi Biblioteca.")

        self.recargarLibros()

    def insertVideojuego(self):
        '''
        Recoge el videojuego seleccionado del listView de películas y lo inserta en la BDD y en la tabla
        '''
        videojuego = self.videojuegos[self.listView_4.currentIndex().row()]

        insertado = Crud.insertarVideojuego(
            self.videojuegos, self.listView_4.currentIndex().row())

        self.contVideojuegos += 1
        if(insertado):
            self.tableVideojuegos.insertRow(self.contVideojuegos)
            self.tableVideojuegos.setRowCount(self.contVideojuegos)

            self.tableVideojuegos.setItem(
                self.contVideojuegos-1, 0, QTableWidgetItem(videojuego[0]))
            self.tableVideojuegos.setItem(
                self.contVideojuegos-1, 1, QTableWidgetItem(videojuego[1]))
            self.tableVideojuegos.setItem(
                self.contVideojuegos-1, 2, QTableWidgetItem(videojuego[2]))
            self.tableVideojuegos.setItem(
                self.contVideojuegos-1, 3, QTableWidgetItem(videojuego[3]))
            self.tableVideojuegos.setItem(
                self.contVideojuegos-1, 4, QTableWidgetItem(videojuego[4]))
            self.infoItemAñadido.setText(
                f"Se ha añadido el videojuego {videojuego[0]}")
            self.infoItemAñadido.exec()
            logging.info(f"Se ha añadido el videojuego {videojuego[0]}")
        else:
            self.infoItemYaAñadido.setText(
                f"El videojuego {videojuego[0]} ya se encuentra en Mi Biblioteca.")
            self.infoItemYaAñadido.exec()
            logging.info(
                f"El videojuego {videojuego[0]} ya se encuentra en Mi Biblioteca.")
        self.recargarVideojuegos()

    def deletePelicula(self):
        '''
        Elimina la pelicula de la BDD y de la tablePeliculas
        '''
        tituloPeliculaActual = self.tablePeliculas.item(self.tablePeliculas.currentRow(),0).text()
        self.msgEliminar.setText(
            '¿Está seguro que desea eliminar la Película?')
        if self.msgEliminar.exec() == QMessageBox.Yes:
            indice = self.tablePeliculas.currentIndex().row()
            Crud.eliminarPelicula(tituloPeliculaActual)
            self.tablePeliculas.removeRow(indice)
            logging.info(f"Se ha eliminado la película con éxito")
        else:
            logging.info('Se ha decidido no eliminar la Película')

    def deleteSerie(self):
        '''
        Elimina la serie de la BDD y de la tableSeries
        '''
        tituloSerieActual = self.tableSeries.item(self.tableSeries.currentRow(),0).text()
        self.msgEliminar.setText('¿Está seguro que desea eliminar la Serie?')
        if self.msgEliminar.exec() == QMessageBox.Yes:
            self.tableSeries.removeRow(self.tableSeries.currentRow())
            Crud.eliminarSerie(tituloSerieActual)
            logging.info(f"Se ha eliminado la serie con éxito")
        else:
            logging.info('Se ha decidido no eliminar la Serie')

    def deleteLibro(self):
        '''
        Elimina el libro de la BDD y de la tableLibros
        '''
        tituloLibroActual = self.tableLibros.item(self.tableLibros.currentRow(),0).text()
        self.msgEliminar.setText('¿Está seguro que desea eliminar el Libro?')
        if self.msgEliminar.exec() == QMessageBox.Yes:
            indice = self.tableLibros.currentIndex().row()
            Crud.eliminarLibro(tituloLibroActual)
            self.tableLibros.removeRow(indice)
            logging.info(f"Se ha eliminado el libro con éxito")
        else:
            logging.info('Se ha decidido no eliminar el Libro')

    def deleteVideojuego(self):
        '''
        Elimina el videojuego de la BDD y de la tableVideojuegos
        '''
        tituloVideojuegoActual = self.tableVideojuegos.item(self.tableVideojuegos.currentRow(),0).text()
        self.msgEliminar.setText(
            '¿Está seguro que desea eliminar el Videojuego?')
        if self.msgEliminar.exec() == QMessageBox.Yes:
            indice = self.tableVideojuegos.currentIndex().row()
            Crud.eliminarVideojuego(tituloVideojuegoActual)
            self.tableVideojuegos.removeRow(indice)
            logging.info(f"Se ha eliminado el videojuego con éxito")
        else:
            logging.info('Se ha decidido no eliminar el Videojuego')

    def tabla_A_Mostrar(self):
        '''
        Muestra una tabla u otra según lo escogido en el comboBox de la pestaña Mi Biblioteca
        '''
        if(self.comboTablas.currentIndex() == 0):
            self.tablePeliculas.setVisible(False)
            self.tableSeries.setVisible(False)
            self.tableLibros.setVisible(False)
            self.tableVideojuegos.setVisible(False)

            self.txtPeliculas.setVisible(False)
            self.txtSeries.setVisible(False)
            self.txtLibros.setVisible(False)
            self.txtVideojuegos.setVisible(False)

        if(self.comboTablas.currentIndex() == 1):
            self.tablePeliculas.setVisible(True)
            self.tableSeries.setVisible(False)
            self.tableLibros.setVisible(False)
            self.tableVideojuegos.setVisible(False)

            self.txtPeliculas.setVisible(True)
            self.txtSeries.setVisible(False)
            self.txtLibros.setVisible(False)
            self.txtVideojuegos.setVisible(False)

        if(self.comboTablas.currentIndex() == 2):
            self.tableSeries.setVisible(True)
            self.tablePeliculas.setVisible(False)
            self.tableLibros.setVisible(False)
            self.tableVideojuegos.setVisible(False)

            self.txtSeries.setVisible(True)
            self.txtPeliculas.setVisible(False)
            self.txtLibros.setVisible(False)
            self.txtVideojuegos.setVisible(False)

        if(self.comboTablas.currentIndex() == 3):
            self.tableLibros.setVisible(True)
            self.tablePeliculas.setVisible(False)
            self.tableSeries.setVisible(False)
            self.tableVideojuegos.setVisible(False)

            self.txtLibros.setVisible(True)
            self.txtPeliculas.setVisible(False)
            self.txtSeries.setVisible(False)
            self.txtVideojuegos.setVisible(False)

        if(self.comboTablas.currentIndex() == 4):
            self.tableVideojuegos.setVisible(True)
            self.tableLibros.setVisible(False)
            self.tablePeliculas.setVisible(False)
            self.tableSeries.setVisible(False)

            self.txtVideojuegos.setVisible(True)
            self.txtLibros.setVisible(False)
            self.txtPeliculas.setVisible(False)
            self.txtSeries.setVisible(False)

    def eliminar(self):
        '''
        Elimina según la tabla que esté visible
        '''
        if self.tableLibros.isVisible():
            self.deleteLibro()
        if self.tableVideojuegos.isVisible():
            self.deleteVideojuego()
        if self.tablePeliculas.isVisible():
            self.deletePelicula()
        if self.tableSeries.isVisible():
            self.deleteSerie()

    def cambiar_A_Inicio(self):
        self.pestanias.setCurrentIndex(0)

    def cambiar_A_Peliculas(self):
        self.pestanias.setCurrentIndex(1)

    def cambiar_A_Series(self):
        self.pestanias.setCurrentIndex(2)

    def cambiar_A_Libros(self):
        self.pestanias.setCurrentIndex(3)

    def cambiar_A_Videojuegos(self):
        self.pestanias.setCurrentIndex(4)

    def cambiar_A_Biblioteca(self):
        self.pestanias.setCurrentIndex(5)

    def cambiar_A_Ayuda(self):
        self.pestanias.setCurrentIndex(6)

    def peliculaTextoFormateado(self, pelicula):
        '''
        Params: pelicula -> lista con datos de la pelicula 
        Return: str formateado con el texto listo para el listView
        '''
        peliculaForm = f"{pelicula[0].upper()}.\n\nAutor: {pelicula[1]}\nReparto: {pelicula[2]}\nSinopsis: {pelicula[3]}\nInformación: {pelicula[4]}\n\n"
        return peliculaForm

    def serieTextoFormateado(self, serie):
        '''
        Params: serie -> lista con datos de la serie 
        Return: str formateado con el texto listo para el listView
        '''
        serieForm = f"{serie[0].upper()}\n\nInformación: {serie[1]}\nDirector: {serie[2]} \nReparto: {serie[3]} \nSinopsis: {serie[4]}\n\n"
        return serieForm

    def libroTextoFormateado(self, libro):
        '''
        Params: libro -> lista con datos del libro 
        Return: str formateado con el texto listo para el listView
        '''
        libroForm = f"{libro[0].upper()}\n\nTemática: {libro[1]}\nAutor: {libro[2]}\nSinopsis: {libro[3]}\nNúmero de páginas: {libro[4]}\n\n"
        return libroForm

    def videojuegoTextoFormateado(self, videojuego):
        '''
        Params: videojuego -> lista con datos del videojuego 
        Return: str formateado con el texto listo para el listView
        '''
        videojuegoForm = f"{videojuego[0].upper()}\n\nFecha de lanzamiento: {videojuego[1]}\nGénero: {videojuego[2]}\nSinopsis: {videojuego[3]}\nPlataformas: {str(videojuego[4])}\n\n"
        return videojuegoForm

    def establecerModelosTablas(self):
        '''
        Definimos las cabeceras de las tablas
        y que no admita selecciones múltiples,
        establecemos el parametro setVisible(False) para que no se muestren al inicio
        '''

        nomColumnasPelicula = ("   TÍTULO   ", "   AUTOR   ",
                               "   REPARTO   ", "     SINOPSIS     ", "   INFORMACIÓN   ")
        nomColumnasSerie = ("   TÍTULO   ", "   INFORMACIÓN   ",
                            "   DIRECTOR   ", "   REPARTO   ", "     SINOPSIS     ")
        nomColumnasLibro = ("   TÍTULO   ", "   TEMÁTICA   ", "   AUTOR   ",
                            "     SINOPSIS     ", "   NÚMERO DE PÁGINAS   ")
        nomColumnasVideojuego = ("   TÍTULO   ", "   FECHA DE LANZAMIENTO   ",
                                 "   GÉNERO  ", "     SINOPSIS     ", "   PLATAFORMAS   ")

        self.tablePeliculas.setHorizontalHeaderLabels(nomColumnasPelicula)
        self.tableSeries.setHorizontalHeaderLabels(nomColumnasSerie)
        self.tableLibros.setHorizontalHeaderLabels(nomColumnasLibro)
        self.tableVideojuegos.setHorizontalHeaderLabels(nomColumnasVideojuego)

        self.tablePeliculas.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tablePeliculas.setSelectionBehavior(QTableWidget.SelectRows)
        self.tablePeliculas.setSelectionMode(QTableWidget.SingleSelection)

        self.tableSeries.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableSeries.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableSeries.setSelectionMode(QTableWidget.SingleSelection)

        self.tableLibros.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableLibros.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableLibros.setSelectionMode(QTableWidget.SingleSelection)

        self.tableVideojuegos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableVideojuegos.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableVideojuegos.setSelectionMode(QTableWidget.SingleSelection)
        self.tablePeliculas.setVisible(False)
        self.tableSeries.setVisible(False)
        self.tableLibros.setVisible(False)
        self.tableVideojuegos.setVisible(False)

    def recargarSeries(self):
        indiceSerie = 0
        querySerie = QSqlQuery()
        querySerie.exec("select * from serie")
        while querySerie.next():
            titulo = querySerie.value(0)
            info = querySerie.value(1)
            director = querySerie.value(2)
            reparto = querySerie.value(3)
            sinopsis = querySerie.value(4)

            self.tableSeries.setRowCount(indiceSerie + 1)

            tituloSerie = QTableWidgetItem(titulo)
            tituloSerie.setToolTip(titulo)
            self.tableSeries.setItem(indiceSerie, 0, tituloSerie)

            infoSerie = QTableWidgetItem(info)
            infoSerie.setToolTip(info)
            self.tableSeries.setItem(indiceSerie, 1, infoSerie)

            directorSerie = QTableWidgetItem(director)
            directorSerie.setToolTip(director)
            self.tableSeries.setItem(indiceSerie, 2, directorSerie)

            repartoSerie = QTableWidgetItem(reparto)
            repartoSerie.setToolTip(reparto)
            self.tableSeries.setItem(indiceSerie, 3, repartoSerie)

            sinopsisSerie = QTableWidgetItem(sinopsis)
            sinopsisSerie.setToolTip(sinopsis)
            self.tableSeries.setItem(indiceSerie, 4, sinopsisSerie)

            indiceSerie += 1

    def recargarPeliculas(self):
        indicePelicula = 0
        queryPelicula = QSqlQuery()
        queryPelicula.exec("select * from pelicula")
        while queryPelicula.next():
            titulo = queryPelicula.value(0)
            autor = queryPelicula.value(1)
            reparto = queryPelicula.value(2)
            sinopsis = queryPelicula.value(3)
            info = queryPelicula.value(4)

            self.tablePeliculas.setRowCount(indicePelicula + 1)

            tituloPelicula = QTableWidgetItem(titulo)
            tituloPelicula.setToolTip(titulo)
            self.tablePeliculas.setItem(indicePelicula, 0, tituloPelicula)

            autorPelicula = QTableWidgetItem(autor)
            autorPelicula.setToolTip(autor)
            self.tablePeliculas.setItem(indicePelicula, 1, autorPelicula)

            repartoPelicula = QTableWidgetItem(reparto)
            repartoPelicula.setToolTip(reparto)
            self.tablePeliculas.setItem(indicePelicula, 2, repartoPelicula)

            sinopsisPelicula = QTableWidgetItem(sinopsis)
            sinopsisPelicula.setToolTip(sinopsis)
            self.tablePeliculas.setItem(indicePelicula, 3, sinopsisPelicula)

            infoPelicula = QTableWidgetItem(info)
            infoPelicula.setToolTip(info)
            self.tablePeliculas.setItem(indicePelicula, 4, infoPelicula)

            indicePelicula += 1

    def recargarLibros(self):
        indiceLibro = 0
        queryLibro = QSqlQuery()
        queryLibro.exec("select * from libro")
        while queryLibro.next():
            titulo = queryLibro.value(0)
            tematica = queryLibro.value(1)
            autor = queryLibro.value(2)
            sinopsis = queryLibro.value(3)
            numPaginas = queryLibro.value(4)

            self.tableLibros.setRowCount(indiceLibro + 1)

            tituloLibro = QTableWidgetItem(titulo)
            tituloLibro.setToolTip(titulo)
            self.tableLibros.setItem(indiceLibro, 0, tituloLibro)

            tematicaLibro = QTableWidgetItem(tematica)
            tematicaLibro.setToolTip(tematica)
            self.tableLibros.setItem(indiceLibro, 1, tematicaLibro)

            autorLibro = QTableWidgetItem(autor)
            autorLibro.setToolTip(autor)
            self.tableLibros.setItem(indiceLibro, 2, autorLibro)

            sinopsisLibro = QTableWidgetItem(sinopsis)
            sinopsisLibro.setToolTip(sinopsis)
            self.tableLibros.setItem(indiceLibro, 3, sinopsisLibro)

            numPagLibro = QTableWidgetItem(numPaginas)
            numPagLibro.setToolTip(numPaginas)
            self.tableLibros.setItem(indiceLibro, 4, numPagLibro)

            indiceLibro += 1

    def recargarVideojuegos(self):
        indiceVideojuego = 0

        queryVideojuego = QSqlQuery()
        queryVideojuego.exec("select * from videojuego")


        
        while queryVideojuego.next():
            titulo = queryVideojuego.value(0)
            fechaLanzamiento = queryVideojuego.value(1)
            genero = queryVideojuego.value(2)
            sinopsis = queryVideojuego.value(3)
            plataformas = queryVideojuego.value(4)

            self.tableVideojuegos.setRowCount(indiceVideojuego + 1)

            tituloVideojuego = QTableWidgetItem(titulo)
            tituloVideojuego.setToolTip(titulo)
            self.tableVideojuegos.setItem(
                indiceVideojuego, 0, tituloVideojuego)

            fechaVideojuego = QTableWidgetItem(fechaLanzamiento)
            fechaVideojuego.setToolTip(fechaLanzamiento)
            self.tableVideojuegos.setItem(indiceVideojuego, 1, fechaVideojuego)

            generoVideojuego = QTableWidgetItem(genero)
            generoVideojuego.setToolTip(genero)
            self.tableVideojuegos.setItem(
                indiceVideojuego, 2, generoVideojuego)

            sinopsisVideojuego = QTableWidgetItem(sinopsis)
            sinopsisVideojuego.setToolTip(sinopsis)
            self.tableVideojuegos.setItem(
                indiceVideojuego, 3, sinopsisVideojuego)

            platafVideojuego = QTableWidgetItem(plataformas)
            platafVideojuego.setToolTip(plataformas)
            self.tableVideojuegos.setItem(
                indiceVideojuego, 4, platafVideojuego)

            indiceVideojuego += 1

    def aniadirPeliculasListView(self):
        '''Rellena el modelo del listView de películas con el modelo adecuado sacado de la lista de películas raspada'''
        if(type(self.peliculas) == None):
            QMessageBox.warning('No se han podido encontrar películas')
        else:
            for p in range(len(self.peliculas)):
                pelicula = self.peliculaTextoFormateado(self.peliculas[p])
                self.modelPelicula.array.append(pelicula)
                self.modelPelicula.layoutChanged.emit()

    def aniadirSeriesListView(self):
        '''Rellena el modelo del listView de series con el modelo adecuado sacado de la lista de series raspada'''
        if(type(self.series) == None):
            QMessageBox.warning('No se han podido encontrar series')
        else:
            for s in range(len(self.series)):
                self.modelSerie.array.append(
                    self.serieTextoFormateado(self.series[s]))
                self.modelSerie.layoutChanged.emit()

    def aniadirVideojuegosListView(self):
        '''Rellena el modelo del listView de videojuegos con el modelo adecuado sacado de la lista de videojuegos raspada'''
        if(type(self.videojuegos) == None):
            QMessageBox.warning('No se han podido encontrar videojuegos')
        else:
            for v in range(len(self.videojuegos)):
                self.modelVideojuego.array.append(
                    self.videojuegoTextoFormateado(self.videojuegos[v]))
                self.modelVideojuego.layoutChanged.emit()

    def aniadirLibrosListView(self):
        '''Rellena el modelo del listView de libros con el modelo adecuado sacado de la lista de libros raspada'''
        if(type(self.libros) == None):
            QMessageBox.warning('No se han podido encontrar libros')
        else:
            for l in range(len(self.libros)):
                self.modelLibro.array.append(
                    self.libroTextoFormateado(self.libros[l]))
                self.modelLibro.layoutChanged.emit()

    def cargarPDFAyuda(self):
        '''
        Cargamos el PDF con el Manual de uso en la pestaña Ayuda
        '''
        layoutVertical = QVBoxLayout()
        self.pestaniaAyuda.setLayout(layoutVertical)
        self.pdf = QWebEngineView()
        self.pdf.setGeometry(450, 30, 300, 600)

        self.pdf.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

        rutaConPDF = Path("Manual de uso Newest.pdf")
        self.pdf.setZoomFactor(2.5)
        self.pdf.load(QUrl(rutaConPDF.absolute().as_uri()))

        layoutVertical.addWidget(self.pdf)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Crud.db_connect('Media', 'QSQLITE')
    ventanaDeCarga = ventanaDeCarga()
    ventanaDeCarga.show()
    sys.exit(app.exec())

