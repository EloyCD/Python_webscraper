from bs4 import BeautifulSoup
import requests

url = 'https://www.encordador.es/'

response = requests.get(url)

if response.status_code == 200:
    
    html_text = response.text

    soup = BeautifulSoup(html_text, 'html.parser')

    cordajes = soup.find_all('div', class_='b-img-t')

    print(cordajes)
        



