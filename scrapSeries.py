import logging
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

import constantes

listaSeries = []


# Funcion para obtener los links de la página
def get_Series_Links(soup):
    lista_box_links = soup.find_all('h2', class_='meta-title')
    links_series = [x.find('a').get('href') for x in lista_box_links]
    return links_series


def obtenerListaSeries():

    try:
        req = requests.get(constantes.WEB_SERIES)

        soup = BeautifulSoup(req.text, 'lxml')
        links = get_Series_Links(soup)

        for l in range(len(links)):
            link = urljoin(constantes.WEB_SERIES, links[l])

            try:

                req_link = requests.get(link)

                serie = []

                soup_link = BeautifulSoup(req_link.text, 'lxml')

                try:
                    titulo = soup_link.find(
                        'div', class_='titlebar-title titlebar-title-lg').get_text(strip=True)
                    serie.append(titulo)
                except:
                    titulo = 'No se ha podido encontrar el título de la serie'
                    serie.append(titulo)

                try:
                    info = soup_link.find(
                        'div', class_='meta-body-item meta-body-info').get_text(strip=True)
                    serie.append(info)
                except:
                    info = 'No se ha podido encontrar la información de la serie'
                    serie.append(info)

                try:
                    director = soup_link.find(
                        'div', class_='meta-body-item meta-body-direction').get_text(strip=True)
                    serie.append(director[10:len(reparto)])
                except:
                    director = 'No se ha podido encontrar el director de la serie'
                    serie.append(director)

                try:
                    reparto = soup_link.find(
                        'div', class_='meta-body-item meta-body-actor').get_text(strip=True)
                    serie.append(reparto[7:len(reparto)])
                except:
                    reparto = 'No se ha podido encontrar el reparto de la serie'
                    serie.append(reparto)

                try:
                    sinopsis = soup_link.find(
                        'div', class_='content-txt').get_text(strip=True)
                    serie.append(sinopsis)
                except:
                    sinopsis = 'No se ha podido encontrar la sinopsis de la serie'
                    serie.append(sinopsis)

                finally:
                    listaSeries.append(serie)
                    req.close()

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

        return listaSeries

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


if __name__ == '__main__':
    obtenerListaSeries()