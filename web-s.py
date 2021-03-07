import requests
from bs4 import BeautifulSoup
import json

URL = 'https://archiveofourown.org/tags/Glee/works'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all(class_="work blurb group")

ficArr = []
for result in results:
    fic = {
        "heading": result.find(class_="heading").text,
        "date": result.find(class_="datetime").text,
        "title": result.find(class_="tags commas").text,
        # "summary": result.find(class_="userstuff summary").text,
        "stats": result.find(class_="stats").text,
    }
    ficArr.append(fic)

with open('ao3Data.json', 'w') as outfile: 
    json.dump(ficArr, outfile)