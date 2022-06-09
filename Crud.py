from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery
import sqlite3
import logging


def db_connect(filename, server):
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
        if not db.open():
            QMessageBox.critical(None, "No se puede abrir la base de datos",
                    "No se puede establecer una conexión con la base de datos.\n"
                    "Este ejemplo necesita compatibilidad con SQLite. Por favor, lea Qt SQL "
                    "documentación del controlador para obtener información sobre cómo construirlo.\n\n"
                    "Haga clic en cancelar para salir.", QMessageBox.Cancel)
            logging.critical('No se ha podido establecer conexión con la base de datos SQLite')
            return False
        else:
            logging.info('Se ha establecido la conexión con la base de datos SQLite')
            return True

def insertarPelicula(peliculas,indice):

    pelicula = peliculas[indice]

    query = QSqlQuery()

    return(query.exec(f"INSERT INTO pelicula VALUES('{pelicula[0]}','{pelicula[1]}','{pelicula[2]}','{pelicula[3]}','{pelicula[4]}') "))

def eliminarPelicula(titulo):

    query = QSqlQuery()
    try:
        query.exec(f'DELETE FROM pelicula WHERE titulo= "{titulo}"')
    except sqlite3.Error as err:
        logging.error(f'Error al eliminar la película con id: {id}')

def insertarSerie(series, indice):

    serie = series[indice]
        
    query = QSqlQuery()

    return(query.exec(f"INSERT INTO serie VALUES('{serie[0]}','{serie[1]}','{serie[2]}','{serie[3]}','{serie[4]}') "))
   
def eliminarLibro(titulo):

    query = QSqlQuery()
    try:
        query.exec(f'DELETE FROM libro WHERE titulo= "{titulo}"')
    except sqlite3.Error as err:
        logging.error(f'Error al eliminar el libro')

def eliminarVideojuego(titulo):

    query = QSqlQuery()
    try:
        query.exec(f'DELETE FROM videojuego WHERE titulo= "{titulo}"')
    except sqlite3.Error as err:
        logging.error(f'Error al eliminar el videojuego',err.message)
    
def insertarLibro(libros, indice):
    libro = (libros[indice])
    query = QSqlQuery()
    return (query.exec(f"INSERT INTO libro VALUES ('{libro[0]}', '{libro[1]}', '{libro[2]}', '{libro[3]}', '{libro[4]}')"))

def insertarVideojuego(videojuegos,indice):
    
    videojuego = videojuegos[indice]

    videojuego[4] = "".join(videojuego[4])
    

    query = QSqlQuery()
    

    return(query.exec( f"INSERT INTO videojuego VALUES('{videojuego[0]}','{videojuego[1]}','{videojuego[2]}','{videojuego[3]}','{videojuego[4]}') "))
       
def eliminarSerie(titulo):
       
    query = QSqlQuery()
    try:
        print(query.exec(f'DELETE FROM serie WHERE titulo= "{titulo}"'))
    except sqlite3.Error as err:
        logging.error(f'Error al eliminar la serie con id: {titulo}',err.message)  
        print('No se ha eliminado la serie')