# Python_webscraper

## Step 1: Installation of the necessary tools

```
beautifulsoup4
lxml
requests

```

## Step 2: Scraping a local HTML file

### `Crea un archivo HTML (home.html)`

Create an HTML file called home.html in your working directory and add the content you want to analyze.

### `Write the Python code:`

```
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)
    # for course in courses_html_tags:
    #     print(course.text)
    course_cards = soup.find_all('div', class_='card' )
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

```

Save the Python script in the same directory as the home.html file and run it. You should see a list of printed links in the console.

## Step 3: Scraping of a real web page

Choose a web page from which you want to extract information. Make sure it is allowed according to the site's terms of service.

### `Write the Python code:`

```
from bs4 import BeautifulSoup
import requests

url = 'https://www.encordador.es/'

response = requests.get(url)

if response.status_code == 200:
    
    html_text = response.text

    soup = BeautifulSoup(html_text, 'html.parser')

    cordajes = soup.find_all('div', class_='b-img-t')

    print(cordajes)

```
Adjust the code to find and extract the specific information you want from the selected web page.

Save the Python script and run it. You should see the extracted information printed in the console.



