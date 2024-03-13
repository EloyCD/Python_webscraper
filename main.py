from bs4 import BeautifulSoup
import requests

# URL de la página web
url = 'https://www.encordador.es/'

# Cordaje que quieres buscar
cordaje_a_buscar = 'Babolat RPM Blast'

# Realizar la solicitud HTTP
response = requests.get(url)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la página
    html_text = response.text

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html_text, 'html.parser')

    # Buscar el cordaje específico en el HTML
    cordajes = soup.find_all('div', class_='b-img-t')

    print(cordajes)
        



