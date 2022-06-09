import requests
from bs4 import BeautifulSoup
import logging
import constantes


listaLibros = []


# Funcion para obtener los links de la página
def get_Book_Links(soup):
    container = soup.find(
        'div', class_='rotador rotador-300 files-visibles-5 files-visibles-mobile-3')
    lista_box_links = container.find_all('li', class_='imatge-gran')
    links_books = [x.find('a').get('href') for x in lista_box_links]
    return links_books


def obtenerListaLibros():

    try:
        req = requests.get(constantes.WEB_LIBROS)

        soup = BeautifulSoup(req.text, 'lxml')
        links = get_Book_Links(soup)

        for l in range(len(links)):
            link = links[l]

            try:
                req_link = requests.get(link)

                libro = []

                soup_link = BeautifulSoup(req_link.text, 'lxml')

                try:
                    titulo = soup_link.find('h1').get_text(strip=True)
                    libro.append(titulo)
                except:
                    titulo = 'No se ha encontrado el título del libro'
                    libro.append(titulo)

                try:
                    tematica = soup_link.find(
                        'div', class_='tematica').get_text(strip=True)
                    libro.append(tematica[9:len(tematica)])
                except:
                    tematica = 'No se ha encontrado la temática de este libro'
                    libro.append(tematica)

                try:
                    autor = soup_link.find(
                        'div', class_='autors').get_text(strip=True)
                    libro.append(autor)
                except:
                    autor = 'No se ha podido encontrar el autor de este libro'
                    libro.append(autor)

                try:
                    sinopsis = soup_link.find(
                        'div', class_='frase-mkt').get_text(strip=True)
                    libro.append(sinopsis)
                except:
                    sinopsis = 'No se ha podido encontrar la sinopsis de este libro'
                    libro.append(sinopsis)

                try:
                    numeroPaginas = soup_link.find(
                        'div', id='num_pagines').get_text(strip=True)
                    libro.append(numeroPaginas)
                except:
                    numeroPaginas = 'No se ha podido encontrar el número de páginas de este libro'
                    libro.append(numeroPaginas)


            except requests.exceptions.HTTPError as errh:
                logging.error(constantes.HTTP_ERROR, errh)
                SystemExit(errh)
            except requests.exceptions.ConnectionError as errc:
                logging.error(constantes.CONNECT_ERROR, errc)
                SystemExit(errc)
            except requests.exceptions.Timeout as errt:
                logging.error(constantes.TIMEOUT_ERROR, errt)
                SystemExit(errt)
            except requests.exceptions.RequestException as err:
                logging.error(constantes.NORMAL_EXCEPTION, err)
                SystemExit(err)
            finally:
                listaLibros.append(libro)

                req_link.close()

        return listaLibros

    except requests.exceptions.HTTPError as errh:
        logging.error(constantes.HTTP_ERROR, errh)
        SystemExit(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error(constantes.CONNECT_ERROR, errc)
        SystemExit(errc)
    except requests.exceptions.Timeout as errt:
        logging.error(constantes.TIMEOUT_ERROR, errt)
        SystemExit(errt)
    except requests.exceptions.RequestException as err:
        logging.error(constantes.NORMAL_EXCEPTION, err)
        SystemExit(err)
    finally:
        req.close()


if __name__ == '__main__':
    obtenerListaLibros()
