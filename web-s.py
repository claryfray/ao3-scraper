import requests
from bs4 import BeautifulSoup

URL = 'https://archiveofourown.org/tags/Glee/works'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="characters")

for result in results:
    print(result.text)