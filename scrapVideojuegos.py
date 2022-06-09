import requests
from bs4 import BeautifulSoup
import logging
import constantes


def obtenerListaVideojuegos():

    fechasLanzamiento = []
    titulosVideojuego=[]
    plataformasVideojuego=[]
    sinopsisVideojuego=[]
    generosVideojuego = []
    listaVideojuegos = []
        
        
    try:    
        req=requests.get(constantes.WEB_VIDEOJUEGOS,timeout=5)

        soup = BeautifulSoup(req.text,'lxml')

        try:
            fechasScrap = soup.find_all('div', class_='tcenter w100 t11')

            for fecha in fechasScrap:
                fechasLanzamiento.append(fecha.get_text(strip=True))
        except:
            fech = 'No se han encontrado fechas a Scrappear'
            fechasLanzamiento.append(fech)

        try:
            titulosScrap = soup.find_all('td', class_='ta14b t11')

            for titulo in titulosScrap:
                titulosVideojuego.append(titulo.find('strong').get_text(strip=True))
        except:
            plataform = 'No se han encontrado titulos a Scrappear'
            titulosVideojuego.append(plataform)

        try:
            #Ancla para encontrar la sinopsis posteriormente
            sinopsis_anclas = soup.find_all('div',class_='fright tcenter')

            for ancla in sinopsis_anclas:
                sinopsisVideojuego.append(ancla.find_next_sibling('p').get_text(strip=True))
        except:
            sinopsis = 'No se ha encontrado sinopsis para este videojuego'
            sinopsisVideojuego.append(sinopsis)
        

        try:
            generosScrap= soup.find_all('div', class_='mt05')

            for genero in generosScrap:
                generosVideojuego.append(genero.get_text())
    
        except:
            generos = 'No se han encontrado géneros para este videojuego'
            generosVideojuego.append(generos)


        try:
            plataformasScrap = soup.find_all('td', class_='ta14b t11')
            for plataforma in plataformasScrap:
                todasPlataformas= plataforma.find_all('span')
                plataformasPorVideojuego = []
                for p in todasPlataformas:
                    plataformasPorVideojuego.append(p.get_text(strip=True))
                plataformasVideojuego.append(plataformasPorVideojuego)         
        except:
            plataform = 'No se han encontrado plataformas para este videojuego'
            plataformasVideojuego.append(plataform)


        for x in range (len(titulosVideojuego)):
            videojuego = []
            videojuego.append(titulosVideojuego[x])
            videojuego.append(fechasLanzamiento[x])
            videojuego.append(generosVideojuego[x])
            videojuego.append(sinopsisVideojuego[x])
            videojuego.append(plataformasVideojuego[x])
            listaVideojuegos.append(videojuego)


        return listaVideojuegos

    except requests.exceptions.HTTPError as errh:
        logging.error(constantes.HTTPError,errh)
        SystemExit(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error(constantes.CONNECT_ERROR,errc)
        SystemExit(errc)
    except requests.exceptions.Timeout as errt:
        logging.error (constantes.TIMEOUT_ERROR,errt)
        SystemExit(errt)
    except requests.exceptions.RequestException as err:
        logging.error (constantes.NORMAL_EXCEPTION,err)
        SystemExit(err)
    finally:
        req.close()

    

if __name__ == '__main__':
    obtenerListaVideojuegos()