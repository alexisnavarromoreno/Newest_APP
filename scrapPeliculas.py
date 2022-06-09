import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging
import constantes


listaPeliculas = []


# Funcion para obtener los links de la página
def get_Peliculas_Links(soup):
    lista_box_links = soup.find_all('h2', class_='meta-title')
    links_peliculas = [x.find('a').get('href') for x in lista_box_links]
    return links_peliculas


def obtenerListaPeliculas():
       
    try:
        req = requests.get(constantes.WEB_PELICULAS)

        soup = BeautifulSoup(req.text , 'lxml')
        links = get_Peliculas_Links(soup)

        for l in range (len(links)):
            link = urljoin(constantes.WEB_PELICULAS,links[l])

            try:
                req_link= requests.get(link)

                pelicula = []

                soup_link = BeautifulSoup(req_link.text, 'lxml')

                try:
                    titulo = soup_link.find('div',class_='titlebar-title titlebar-title-lg').get_text(strip=True)
                    pelicula.append(titulo)
                except:
                    titulo = 'El titulo de esta pelicula no se ha encontrado'
                    pelicula.append(titulo)

                try:
                    autor = soup_link.find('div', class_='meta-body-item meta-body-direction').get_text(strip=True)
                    pelicula.append(autor[12:len(autor)])
                except:
                    autor= 'El autor de esta película no se ha encontrado'
                    pelicula.append(autor)

                try:
                    reparto = soup_link.find('div', class_='meta-body-item meta-body-actor').get_text(strip=True)
                    pelicula.append(reparto[7:len(reparto)])
                except:
                    reparto= 'El reparto de esta pelicula no se ha encontrado'
                    pelicula.append(reparto)
           
                try:
                    sinopsis = soup_link.find('div', class_='content-txt').get_text(strip=True)
                    pelicula.append(sinopsis)
                except:
                    sinopsis= 'La sinopsis de esta película no se ha encontrado'
                    pelicula.append(sinopsis)

                try:
                    info = soup_link.find('div',class_='meta-body-item meta-body-info').get_text(strip=True)
                    pelicula.append(info)
                except :
                    info = 'No se ha encontrado información sobre esta película'
                    pelicula.append(info)

                
                listaPeliculas.append(pelicula)
                req_link.close()
                req.close()

            except requests.exceptions.HTTPError as errh:
                logging.error (constantes.HTTP_ERROR,errh)
                SystemExit(errh)
            except requests.exceptions.ConnectionError as errc:
                logging.error (constantes.CONNECT_ERROR,errc)
                SystemExit(errc)
            except requests.exceptions.Timeout as errt:
                logging.error (constantes.TIMEOUT_ERROR,errt)
                SystemExit(errt)
            except requests.exceptions.RequestException as err:
                logging.error (constantes.NORMAL_EXCEPTION,err)
                SystemExit(err)
                
        return listaPeliculas

    except requests.exceptions.HTTPError as errh:
        logging.error (constantes.HTTP_ERROR,errh)
        SystemExit(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error (constantes.CONNECT_ERROR,errc)
        SystemExit(errc)
    except requests.exceptions.Timeout as errt:
        logging.error (constantes.TIMEOUT_ERROR,errt)
        SystemExit(errt)
    except requests.exceptions.RequestException as err:
        logging.error (constantes.NORMAL_EXCEPTION,err)
        SystemExit(err)
    

if __name__ == '__main__':
    obtenerListaPeliculas()



