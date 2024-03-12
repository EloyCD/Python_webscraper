from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.udemy.com/courses/search/?src=ukw&q=python').text
soup = BeautifulSoup(html_text, 'lxml')
courses = soup.find_all()
print(courses)