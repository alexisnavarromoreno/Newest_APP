import unittest
import scrapPeliculas
import scrapSeries
import scrapLibros
import scrapVideojuegos

class testScrap(unittest.TestCase):


    def testListaPeliculas(self):
        self.assertIsNotNone(scrapPeliculas.obtenerListaPeliculas(),'No se ha obtenido correctamente la lista de peliculas')

    def testListaSeries(self):
        self.assertIsNotNone(scrapSeries.obtenerListaSeries(),'No se ha obtenido correctamente la lista de series')

    def testListaLibros(self):
        self.assertIsNotNone(scrapLibros.obtenerListaLibros(),'No se ha obtenido correctamente la lista de libros')

    def testListaVideojuegos(self):
        self.assertIsNotNone(scrapVideojuegos.obtenerListaVideojuegos(),'No se ha podido obtener la lista de videojuegos')
    

if __name__=="__main__":
    unittest.main()