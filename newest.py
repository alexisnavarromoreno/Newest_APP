# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'newest.ui'
##
# Created by: Qt User Interface Compiler version 6.2.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QUrl)
from PySide6.QtWebEngineWidgets import *
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
                               QListView, QMainWindow, QMenu, QMenuBar,
                               QPushButton, QScrollArea, QSizePolicy, QStatusBar,
                               QTabWidget, QTableWidget, QToolBar, QVBoxLayout,
                               QWidget, QComboBox, QMessageBox)
from PySide6 import QtCore
import resourcesQrc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 789)
        icon = QIcon()
        icon.addFile(u":/iconos/iconoNewest.ico",
                     QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u'''QMainWindow::separator {
     background: yellow;
     width: 10px; /* when vertical */
     height: 10px; /* when horizontal */
 }
    
 QMainWindow::separator:hover {
     background: red;
 }''')
        self.actionPeliculas = QAction(MainWindow)
        self.actionPeliculas.setObjectName(u"actionPeliculas")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconoPeliculaSerie.ico",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionPeliculas.setIcon(icon1)
        self.actionLibros = QAction(MainWindow)
        self.actionLibros.setObjectName(u"actionLibros")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconoLibro.ico",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionLibros.setIcon(icon2)
        self.actionSeries = QAction(MainWindow)
        self.actionSeries.setObjectName(u"actionSeries")
        self.actionSeries.setIcon(icon1)
        self.actionVideojuegos = QAction(MainWindow)
        self.actionVideojuegos.setObjectName(u"actionVideojuegos")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconoVideojuego.ico",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionVideojuegos.setIcon(icon3)
        self.actionMi_biblioteca = QAction(MainWindow)
        self.actionMi_biblioteca.setObjectName(u"actionMi_biblioteca")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/iconoFavoritos.ico",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.actionMi_biblioteca.setIcon(icon4)
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/home.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHome.setIcon(icon5)
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/ayuda.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAyuda.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pestanias = QTabWidget(self.centralwidget)
        self.pestanias.setObjectName(u"pestanias")
        self.pestanias.setStyleSheet(u"QTabWidget::pane {\n"
                                     "  border: 1px solid lightgray;\n"
                                     "  top:-1px; \n"
                                     "  background-color: rgb(0, 0, 0); \n"
                                     "} \n"
                                     "\n"
                                     "  QTabWidget::tab-bar {\n"
                                     "     alignment: center;\n"
                                     "  }\n"

                                     "QTabBar::tab {\n"
                                     "  background-color: rgb(0, 0, 0); \n"
                                     "color: rgb(255, 255, 255)\n;"
                                     "border-radius: 10px;\n;"
                                     "  border: 1px solid lightgray; \n"
                                     "  padding: 15px;\n"
                                     "margin: 5px;} \n"
                                     "\n"
                                     "QTabBar::tab:selected { \n"
                                     "  background: #ffee66; \n"
                                     "color: rgb(0, 0, 0)\n;"
                                     "border-radius: 10px;\n;"
                                     "  margin-bottom: -1px; \n"
                                     "}")
        self.pestanias.setTabPosition(QTabWidget.North)
        self.pestanias.setDocumentMode(False)
        self.pestaniaInicio = QWidget()
        self.pestaniaInicio.setObjectName(u"pestaniaInicio")
        self.verticalLayout_11 = QVBoxLayout(self.pestaniaInicio)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scrollArea_5 = QScrollArea(self.pestaniaInicio)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(
            u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 783, 625))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"QWidget#scrollAreaWidgetContents_6{"
                                                      "background-color:qlineargradient(spread:pad, x1:0, y1:0.04, x2:0.965149, y2:0.983, stop:0 rgba(231, 215, 92, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.labelBienvenido = QLabel(self.scrollAreaWidgetContents_6)
        self.labelBienvenido.setObjectName(u"labelBienvenido")
        self.labelBienvenido.setText("Bienvenido a <strong>Newest<\strong>")
        self.labelBienvenido.setStyleSheet(
            'font: 36pt "MS Shell Dlg 2"; color: rgb(255, 255, 255); margin:15px;')
        self.labelBienvenido.setAlignment(Qt.AlignCenter)
        self.labelBienvenido .setScaledContents(True)
        self.verticalLayout_12.addWidget(self.labelBienvenido)
        self.label = QLabel(self.scrollAreaWidgetContents_6)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/iconos/logo.PNG"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setMargin(5)
        self.label.setIndent(1)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_12.addWidget(self.label)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setStyleSheet(
            'font: 18pt "MS Shell Dlg 2"; margin:15px; color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 0, 0, 255))')
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setMargin(4)

        self.verticalLayout_12.addWidget(self.label_2)

        self.labelAnuncio = QLabel(self.scrollAreaWidgetContents_6)
        self.labelAnuncio.setObjectName(u"labelAnuncio")
        self.labelAnuncio.setText(
            "Explore más de mis <strong>Proyectos<\strong> en el siguiente link:")
        self.labelAnuncio.setStyleSheet(
            'font: 14pt "MS Shell Dlg 2"; color: rgb(0, 0, 0)')
        self.labelAnuncio.setAlignment(Qt.AlignCenter)
        self.labelAnuncio .setScaledContents(True)
        self.verticalLayout_12.addWidget(self.labelAnuncio)

        self.labelLink = QLabel(self.scrollAreaWidgetContents_6)
        self.labelLink.setObjectName(u"labelLink")
        self.labelLink.setText(
            '<a href="https://alexisnavarromoreno.github.io/">https://alexisnavarromoreno.github.io//</a>')
        self.labelLink.setStyleSheet(
            'font: 14pt "MS Shell Dlg 2"; color: rgb(255, 255, 255)')
        self.labelLink.setTextFormat(QtCore.Qt.RichText)
        self.labelLink.setTextInteractionFlags(
            QtCore.Qt.TextBrowserInteraction)
        self.labelLink.setOpenExternalLinks(True)
        self.labelLink.setGeometry(QtCore.QRect(360, 310, 58, 18))
        self.labelLink.setAlignment(Qt.AlignCenter)
        self.labelLink .setScaledContents(True)
        self.verticalLayout_12.addWidget(self.labelLink)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_11.addWidget(self.scrollArea_5)

        self.pestanias.addTab(self.pestaniaInicio, icon5, "")
        self.pestaniaPeliculas = QWidget()
        self.pestaniaPeliculas.setObjectName(u"pestaniaPeliculas")
        self.gridLayout_2 = QGridLayout(self.pestaniaPeliculas)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.pestaniaPeliculas)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 783, 625))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.botonAniadirPelicula = QPushButton(self.scrollAreaWidgetContents)
        self.botonAniadirPelicula.setObjectName(u"botonAniadirPelicula")
        self.botonAniadirPelicula.setStyleSheet(u"box-shadow:inset 0px 1px 0px 0px #3CC8A2;\n"
                                                "	background-color:#000000;\n"
                                                "	border-radius:6px;\n"
                                                "	border:1px solid #4DFACB;\n"
                                                "	display:inline-block;\n"
                                                "	cursor:pointer;\n"
                                                "	color:#4DFACB;\n"
                                                "font: 14pt 'Segoe UI';"
                                                "	font-weight:bold;\n"
                                                "	padding:20px;\n"
                                                "	text-decoration:none;\n"
                                                "	text-shadow:0px 1px 0px #3CC8A2;")

        self.gridLayout_3.addWidget(self.botonAniadirPelicula, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.gridLayout_3.addLayout(self.verticalLayout_9, 2, 0, 1, 1)

        self.listView = QListView(self.scrollAreaWidgetContents)
        self.listView.setObjectName(u"listView")
        self.listView.setStyleSheet(
            'QListView {'
            'show-decoration-selected: 1; '
            'border-radius: 25px;'
            'font-weight:bold;\n }'
            'QListView::item:alternate {'
            'color: rgb(0, 0, 0);'
            'background: #EEEEEE;}'

            'QListView::item:selected {'
            'color: rgb(0, 0, 0);'
            'border: 1px solid #6a6ea9;'
            '}'

            'QListView::item:selected:!active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'


            'QListView::item:selected:active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);'
            'font-weight: bold;}'

            'QListView::item:hover {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'
        )
        self.listView.setFont(font)

        self.gridLayout_3.addWidget(self.listView, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.pestanias.addTab(self.pestaniaPeliculas, icon1, "")
        self.pestaniaSeries = QWidget()
        self.pestaniaSeries.setObjectName(u"pestaniaSeries")
        self.verticalLayout_3 = QVBoxLayout(self.pestaniaSeries)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_2 = QScrollArea(self.pestaniaSeries)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 783, 625))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listView_2 = QListView(self.scrollAreaWidgetContents_2)
        self.listView_2.setStyleSheet(
            'QListView {'
            'show-decoration-selected: 1; '
            'border-radius: 25px;'
            'font-weight:bold;\n }'
            'QListView::item:alternate {'
            'color: rgb(0, 0, 0);'
            'background: #EEEEEE;}'

            'QListView::item:selected {'
            'color: rgb(0, 0, 0);'
            'border: 1px solid #6a6ea9;'
            '}'

            'QListView::item:selected:!active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'


            'QListView::item:selected:active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);'
            'font-weight: bold;}'

            'QListView::item:hover {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'
        )
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setFont(font)

        self.gridLayout_4.addWidget(self.listView_2, 0, 0, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.gridLayout_4.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.botonAniadirSerie = QPushButton(self.scrollAreaWidgetContents_2)
        self.botonAniadirSerie.setObjectName(u"botonAniadirSerie")
        self.botonAniadirSerie.setStyleSheet(u"box-shadow:inset 0px 1px 0px 0px #3CC8A2;\n"
                                             "	background-color:#000000;\n"
                                             "	border-radius:6px;\n"
                                             "	border:1px solid #4DFACB;\n"
                                             "	display:inline-block;\n"
                                             "	cursor:pointer;\n"
                                             "	color:#4DFACB;\n"
                                             "font: 14pt 'Segoe UI';"
                                             "	font-weight:bold;\n"
                                             "	padding:20px;\n"
                                             "	text-decoration:none;\n"
                                             "	text-shadow:0px 1px 0px #3CC8A2;")

        self.gridLayout_4.addWidget(self.botonAniadirSerie, 2, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea_2)

        self.pestanias.addTab(self.pestaniaSeries, icon1, "")
        self.pestaniaLibros = QWidget()
        self.pestaniaLibros.setObjectName(u"pestaniaLibros")
        self.verticalLayout_4 = QVBoxLayout(self.pestaniaLibros)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_3 = QScrollArea(self.pestaniaLibros)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(
            u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 783, 625))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.listView_3 = QListView(self.scrollAreaWidgetContents_3)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setStyleSheet(
            'QListView {'
            'show-decoration-selected: 1;\n'
            'border-radius: 25px;'
            'font-weight:bold;\n }'

            'QListView::item:alternate {'
            'color: rgb(0, 0, 0);'
            'background: #EEEEEE;}'

            'QListView::item:selected {'
            'border: 1px solid #6a6ea9;'
            'color: rgb(0, 0, 0);'
            '}'

            'QListView::item:selected:!active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'


            'QListView::item:selected:active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);'
            'font-weight: bold;}'

            'QListView::item:hover {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'
        )

        self.listView_3.setFont(font)
        self.gridLayout_5.addWidget(self.listView_3, 0, 0, 1, 1)

        self.botonAniadirLibro = QPushButton(self.scrollAreaWidgetContents_3)
        self.botonAniadirLibro.setObjectName(u"botonAniadirLibro")
        self.botonAniadirLibro.setStyleSheet(u"box-shadow:inset 0px 1px 0px 0px #3CC8A2;\n"
                                             "	background-color:#000000;\n"
                                             "	border-radius:6px;\n"
                                             "	border:1px solid #4DFACB;\n"
                                             "	display:inline-block;\n"
                                             "	cursor:pointer;\n"
                                             "	color:#4DFACB;\n"
                                             "font: 14pt 'Segoe UI'; "
                                             "	font-weight:bold;\n"
                                             "	padding:20px;\n"
                                             "	text-decoration:none;\n"
                                             "	text-shadow:0px 1px 0px #3CC8A2;")

        self.gridLayout_5.addWidget(self.botonAniadirLibro, 1, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.gridLayout_5.addLayout(self.verticalLayout_7, 2, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_3)

        self.pestanias.addTab(self.pestaniaLibros, icon2, "")
        self.pestaniaVideojuegos = QWidget()
        self.pestaniaVideojuegos.setObjectName(u"pestaniaVideojuegos")
        self.verticalLayout_5 = QVBoxLayout(self.pestaniaVideojuegos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_4 = QScrollArea(self.pestaniaVideojuegos)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(
            u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 783, 625))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.botonAniadirVideojuego = QPushButton(
            self.scrollAreaWidgetContents_4)
        self.botonAniadirVideojuego.setObjectName(u"botonAniadirVideojuego")
        self.botonAniadirVideojuego.setStyleSheet(u"box-shadow:inset 0px 1px 0px 0px #3CC8A2;\n"
                                                  "	background-color:#000000;\n"
                                                  "	border-radius:6px;\n"
                                                  "	border:1px solid #4DFACB;\n"
                                                  "	display:inline-block;\n"
                                                  "	cursor:pointer;\n"
                                                  "	color:#4DFACB;\n"
                                                  "	font: 14pt 'Segoe UI';\n"
                                                  "	font-weight:bold;\n"
                                                  "	padding:20px;\n"
                                                  "	text-decoration:none;\n"
                                                  "	text-shadow:0px 1px 0px #3CC8A2;")

        self.gridLayout_6.addWidget(self.botonAniadirVideojuego, 2, 0, 1, 1)

        self.listView_4 = QListView(self.scrollAreaWidgetContents_4)
        self.listView_4.setObjectName(u"listView_4")
        self.listView_4.setStyleSheet(
            'QListView {'
            'show-decoration-selected: 1;\n'
            'border-radius: 25px;'
            'font-weight:bold;\n }'

            'QListView::item:alternate {'
            'background: #EEEEEE;}'

            'QListView::item:selected {'
            'border: 1px solid #6a6ea9;'
            'color: rgb(0, 0, 0);'
            '}'

            'QListView::item:selected:!active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'


            'QListView::item:selected:active {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);'
            'font-weight: bold;}'

            'QListView::item:hover {'
            'color: rgb(0, 0, 0);'
            'background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,'
            'stop: 0 #ffee66, stop: 1 #ffffff);}'
        )

        self.listView_4.setFont(font)
        self.gridLayout_6.addWidget(self.listView_4, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.gridLayout_6.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.scrollArea_4)

        self.pestanias.addTab(self.pestaniaVideojuegos, icon3, "")
        self.pestaniaBiblioteca = QWidget()
        self.pestaniaBiblioteca.setObjectName(u"pestaniaBiblioteca")
        self.verticalLayout_6 = QVBoxLayout(self.pestaniaBiblioteca)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollBiblioteca = QScrollArea(self.pestaniaBiblioteca)
        self.scrollBiblioteca.setObjectName(u"scrollBiblioteca")
        self.scrollBiblioteca.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(
            u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 762, 974))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtPeliculas = QLabel(self.scrollAreaWidgetContents_5)
        self.txtPeliculas.setObjectName(u"txtPeliculas")

        self.txtPeliculas.setStyleSheet('font: 19pt "Segoe UI";;\n'
                                        'padding: 5px;\n'
                                        'font-weight:bold;\n')
        self.txtPeliculas.setScaledContents(False)
        self.txtPeliculas.setAlignment(Qt.AlignCenter)
        self.txtPeliculas.setWordWrap(True)
        self.txtPeliculas.setTextInteractionFlags(Qt.NoTextInteraction)

        self.comboTablas = QComboBox()
        self.comboTablas.addItem('¿Qué quieres mostrar?')
        self.comboTablas.addItem('Peliculas')
        self.comboTablas.addItem('Series')
        self.comboTablas.addItem('Libros')
        self.comboTablas.addItem('Videojuegos')
        self.comboTablas.setStyleSheet('background-color: #FFF67F;\n'
                                       'font-weight:bold;'
                                       'color: #000000;\n'
                                       'font: 18pt "Segoe UI";\n'
                                       'padding: 10px;\n')
        self.verticalLayout.addWidget(self.comboTablas)
        self.verticalLayout.addWidget(self.txtPeliculas)

        self.tablePeliculas = QTableWidget(self.scrollAreaWidgetContents_5)
        self.tablePeliculas.setObjectName(u"tablePeliculas")

        self.verticalLayout.addWidget(self.tablePeliculas)

        self.txtSeries = QLabel(self.scrollAreaWidgetContents_5)
        self.txtSeries.setObjectName(u"txtSeries")
        self.txtSeries.setStyleSheet('font: 19pt "Segoe UI";\n'
                                     'padding: 5px;\n'
                                     'font-weight:bold;\n')
        self.txtSeries.setScaledContents(True)
        self.txtSeries.setAlignment(Qt.AlignCenter)
        self.txtSeries.setWordWrap(True)
        self.txtSeries.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.txtSeries)

        self.tableSeries = QTableWidget(self.scrollAreaWidgetContents_5)
        self.tableSeries.setObjectName(u"tableSeries")

        self.verticalLayout.addWidget(self.tableSeries)

        self.txtLibros = QLabel(self.scrollAreaWidgetContents_5)
        self.txtLibros.setObjectName(u"txtLibros")
        self.txtLibros.setStyleSheet('font: 19pt "Segoe UI";\n'
                                     'padding: 5px;\n'
                                     'font-weight:bold;\n')
        self.txtLibros.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txtLibros)

        self.tableLibros = QTableWidget(self.scrollAreaWidgetContents_5)
        self.tableLibros.setObjectName(u"tableLibros")

        self.verticalLayout.addWidget(self.tableLibros)

        self.txtVideojuegos = QLabel(self.scrollAreaWidgetContents_5)
        self.txtVideojuegos.setObjectName(u"txtVideojuegos")
        self.txtVideojuegos.setStyleSheet('font: 19pt "Segoe UI";\n'
                                          'padding: 5px;\n'
                                          'font-weight:bold;\n')
        self.txtVideojuegos.setScaledContents(True)
        self.txtVideojuegos.setAlignment(Qt.AlignCenter)
        self.txtVideojuegos.setWordWrap(True)

        self.verticalLayout.addWidget(self.txtVideojuegos)

        self.tableVideojuegos = QTableWidget(self.scrollAreaWidgetContents_5)
        self.tableVideojuegos.setObjectName(u"tableVideojuegos")

        self.verticalLayout.addWidget(self.tableVideojuegos)

        self.botonEliminarBiblioteca = QPushButton(
            self.scrollAreaWidgetContents_5)
        self.botonEliminarBiblioteca.setObjectName(u"botonEliminarBiblioteca")
        self.botonEliminarBiblioteca.setStyleSheet(u"box-shadow:inset 0px 1px 0px 0px #f29c93;\n"
                                                   "	background-color:#000000;\n"
                                                   "	border-radius:6px;\n"
                                                   "	border:1px solid #d83526;\n"
                                                   "	display:inline-block;\n"
                                                   "	cursor:pointer;\n"
                                                   "	color:#d83526;\n"
                                                   "	font: 19pt 'Segoe UI';"
                                                   "	font-weight:bold;\n"
                                                   "	padding:20px;\n"
                                                   "	text-decoration:none;\n"
                                                   "	text-shadow:0px 1px 0px #9E1F1F;")
        icon7 = QIcon()
        icon7.addFile(u":/iconosApp/resourcesApp/iconoEliminar.ico",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.botonEliminarBiblioteca.setIcon(icon7)

        self.verticalLayout.addWidget(self.botonEliminarBiblioteca)

        self.gridLayout_7.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollBiblioteca.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_6.addWidget(self.scrollBiblioteca)

        self.pestanias.addTab(self.pestaniaBiblioteca, icon4, "")
        self.pestaniaAyuda = QWidget()

        self.pestaniaAyuda.setObjectName(u"pestaniaAyuda")
        self.pestanias.addTab(self.pestaniaAyuda, icon6, "")
        self.verticalLayout_10.addWidget(self.pestanias)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 831, 26))
        self.menubar.setStyleSheet(u"")
        self.menuSeleccionar = QMenu(self.menubar)
        self.menuSeleccionar.setObjectName(u"menuSeleccionar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuSeleccionar.menuAction())
        self.menuSeleccionar.addAction(self.actionHome)
        self.menuSeleccionar.addAction(self.actionAyuda)
        self.menuSeleccionar.addAction(self.actionPeliculas)
        self.menuSeleccionar.addAction(self.actionSeries)
        self.menuSeleccionar.addAction(self.actionLibros)
        self.menuSeleccionar.addAction(self.actionVideojuegos)
        self.menuSeleccionar.addAction(self.actionMi_biblioteca)

        self.botonAniadirLibro.setIcon(QIcon('iconoAniadir.ico'))
        self.botonAniadirSerie.setIcon(QIcon('iconoAniadir.ico'))
        self.botonAniadirPelicula.setIcon(QIcon('iconoAniadir.ico'))
        self.botonAniadirVideojuego.setIcon(QIcon('iconoAniadir.ico'))
        self.botonEliminarBiblioteca.setIcon(QIcon('iconoEliminar.ico'))

        self.tablePeliculas.setAlternatingRowColors(True)
        self.tableSeries.setAlternatingRowColors(True)
        self.tableLibros.setAlternatingRowColors(True)
        self.tableVideojuegos.setAlternatingRowColors(True)
        self.tableVideojuegos.setStyleSheet('''QTableView
{
    gridline-color: #BCBCBC;
    font: 14pt "Segoe UI";
    border: 1px solid #000;
}

QTableView QTableCornerButton::section
{
    background-color: #FCFCFC;
    border: 1px solid #000;
}
QHeaderView::section {
    background-color: #FFF67F;
    border: 1px solid #000;
    font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::selected
{
    selection-background-color: #FFF67F;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::hover
{
    background-color: #C8EDFF;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}''')

        self.tablePeliculas.setStyleSheet('''QTableView
{
    gridline-color: #BCBCBC;
    font: 14pt "Segoe UI";
    border: 1px solid #000;
}

QTableView QTableCornerButton::section
{
    background-color: #FCFCFC;
    border: 1px solid #000;
}
QHeaderView::section {
    background-color: #FFF67F;
    border: 1px solid #000;
    font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::selected
{
    selection-background-color: #FFF67F;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::hover
{
    background-color: #C8EDFF;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}''')

        self.tableSeries.setStyleSheet('''QTableView
{
    gridline-color: #BCBCBC;
    font: 14pt "Segoe UI";
    border: 1px solid #000;
}

QTableView QTableCornerButton::section
{
    background-color: #FCFCFC;
    border: 1px solid #000;
}
QHeaderView::section {
    background-color: #FFF67F;
    border: 1px solid #000;
    font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::selected
{
    selection-background-color: #FFF67F;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::hover
{
    background-color: #C8EDFF;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}''')

        self.tableLibros.setStyleSheet('''QTableView
{
    gridline-color: #BCBCBC;
    font: 14pt "Segoe UI";
    font-family: Arial;
    border: 1px solid #000;
}

QTableView QTableCornerButton::section
{
    background-color: #FCFCFC;
    border: 1px solid #000;
}
QHeaderView::section {
    background-color: #FFF67F;
    border: 1px solid #000;
    font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::selected
{
    selection-background-color: #FFF67F;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}

QTableView::item::hover
{
    background-color: #C8EDFF;
    selection-color:black;
    border: 1px solid #000;
     font-weight: bold;
    font: 14pt "Segoe UI";
}''')
        self.tablePeliculas.setColumnCount(5)
        self.tableSeries.setColumnCount(5)
        self.tableLibros.setColumnCount(5)
        self.tableVideojuegos.setColumnCount(5)

        self.listView.setSpacing(10)
        self.listView_2.setSpacing(10)
        self.listView_3.setSpacing(10)
        self.listView_4.setSpacing(10)

        self.listView.setStatusTip(
            'Seleccione una película para añadir a la biblioteca')
        self.listView.setToolTip('Seleccione una película')
        self.listView_2.setStatusTip(
            'Seleccione una serie para añadir a la biblioteca')
        self.listView_2.setToolTip('Seleccione una serie')
        self.listView_3.setStatusTip(
            'Seleccione un libro para añadir a la biblioteca')
        self.listView_3.setToolTip('Seleccione un libro')
        self.listView_4.setStatusTip(
            'Seleccione un videojuego para añadir a la biblioteca')
        self.listView_4.setToolTip('Seleccione un videojuego')

        self.tablePeliculas.setStatusTip(
            'Seleccione una pelicula para eliminar de la biblioteca')
        self.tablePeliculas.setToolTip('Seleccione una película')
        self.tableSeries.setStatusTip(
            'Seleccione una serie eliminar de la biblioteca')
        self.tableSeries.setToolTip('Seleccione una serie')
        self.tableLibros.setStatusTip(
            'Seleccione un libro para eliminar de la biblioteca')
        self.tableLibros.setToolTip('Seleccione un libro')
        self.tableVideojuegos.setStatusTip(
            'Seleccione un videojuego para eliminar de la biblioteca')
        self.tableVideojuegos.setToolTip('Seleccione un videojuego')
        
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
   

        self.msgEliminar = QMessageBox()
        self.msgEliminar.setIcon(QMessageBox.Question)
        self.msgEliminar.setWindowTitle("Eliminar")
        self.msgEliminar.setStandardButtons(QMessageBox.Yes)
        self.msgEliminar.addButton(QMessageBox.No)
        self.msgEliminar.setDefaultButton(QMessageBox.Yes)
   


        self.retranslateUi(MainWindow)

        self.pestanias.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Newest", None))
        self.actionPeliculas.setText(
            QCoreApplication.translate("MainWindow", u"Peliculas", None))
# if QT_CONFIG(shortcut)
        self.actionPeliculas.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionLibros.setText(
            QCoreApplication.translate("MainWindow", u"Libros", None))
# if QT_CONFIG(shortcut)
        self.actionLibros.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionSeries.setText(
            QCoreApplication.translate("MainWindow", u"Series", None))
# if QT_CONFIG(shortcut)
        self.actionSeries.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionVideojuegos.setText(
            QCoreApplication.translate("MainWindow", u"Videojuegos", None))
# if QT_CONFIG(shortcut)
        self.actionVideojuegos.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionMi_biblioteca.setText(
            QCoreApplication.translate("MainWindow", u"Mi biblioteca", None))
# if QT_CONFIG(shortcut)
        self.actionMi_biblioteca.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionHome.setText(QCoreApplication.translate(
            "MainWindow", u"Inicio", None))
# if QT_CONFIG(tooltip)
        self.actionHome.setToolTip(
            QCoreApplication.translate("MainWindow", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(shortcut)
        self.actionHome.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionAyuda.setText(
            QCoreApplication.translate("MainWindow", u"Ayuda", None))
# if QT_CONFIG(shortcut)
        self.actionAyuda.setShortcut(
            QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
# if QT_CONFIG(tooltip)
        self.pestanias.setToolTip("Elige una categoría")
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.pestanias.setStatusTip("Elige una categoría")
#endif // QT_CONFIG(statustip)
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"¿Cansado de consultar distintas webs para saber cuales son las novedades que te interesan? Newest, tu APP para consultar novedades te ofrece la posiblida de tenerlas todas a tu alcance. Navega por las distintas pestañas y descubre lo que te ofrece, añade a Mi Biblioteca los títulos en los que estás interesado y eliminalos cuando quieras.", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaInicio), QCoreApplication.translate("MainWindow", u"Inicio", None))
# if QT_CONFIG(tooltip)
        self.pestanias.setTabToolTip(self.pestanias.indexOf(
            self.pestaniaInicio), QCoreApplication.translate("MainWindow", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(tooltip)
        self.botonAniadirPelicula.setToolTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir pelicula", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.botonAniadirPelicula.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir pel\u00edcula a mi biblioteca", None))
#endif // QT_CONFIG(statustip)
        self.botonAniadirPelicula.setText(
            QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaPeliculas), QCoreApplication.translate("MainWindow", u"Peliculas", None))
# if QT_CONFIG(tooltip)
        self.botonAniadirSerie.setToolTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir serie", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.botonAniadirSerie.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir serie a mi biblioteca", None))
#endif // QT_CONFIG(statustip)
        self.botonAniadirSerie.setText(
            QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaSeries), QCoreApplication.translate("MainWindow", u"Series", None))
# if QT_CONFIG(tooltip)
        self.botonAniadirLibro.setToolTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir libro", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.botonAniadirLibro.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir libro a mi biblioteca", None))
#endif // QT_CONFIG(statustip)
        self.botonAniadirLibro.setText(
            QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaLibros), QCoreApplication.translate("MainWindow", u"Libros", None))
# if QT_CONFIG(tooltip)
        self.botonAniadirVideojuego.setToolTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir videojuego", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.botonAniadirVideojuego.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"A\u00f1adir videojuego a mi biblioteca", None))
#endif // QT_CONFIG(statustip)
        self.botonAniadirVideojuego.setText(
            QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaVideojuegos), QCoreApplication.translate("MainWindow", u"Videojuegos", None))
        self.txtPeliculas.setText(QCoreApplication.translate(
            "MainWindow", u"Pel\u00edculas", None))
        self.txtSeries.setText(QCoreApplication.translate(
            "MainWindow", u"Series", None))
        self.txtLibros.setText(QCoreApplication.translate(
            "MainWindow", u"Libros", None))
        self.txtVideojuegos.setText(QCoreApplication.translate(
            "MainWindow", u"Videojuegos", None))
# if QT_CONFIG(tooltip)
        self.botonEliminarBiblioteca.setToolTip(
            QCoreApplication.translate("MainWindow", u"Eliminar", None))
#endif // QT_CONFIG(tooltip)
# if QT_CONFIG(statustip)
        self.botonEliminarBiblioteca.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Eliminar de mi biblioteca", None))
#endif // QT_CONFIG(statustip)
        self.botonEliminarBiblioteca.setText(
            QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaBiblioteca), QCoreApplication.translate("MainWindow", u"Mi biblioteca", None))
        self.pestanias.setTabText(self.pestanias.indexOf(
            self.pestaniaAyuda), QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.menuSeleccionar.setTitle(
            QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"toolBar", None))

    # retranslateUi
