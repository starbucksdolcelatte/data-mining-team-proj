
'''
me02_view_cont02 > table > tbody
    'me02_view_cont01 > p'
'''
# parser.py
import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('http://kkc.or.kr/megazine/megazine_02_view.html?idx=3&page=1&key=')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(

    'body > div.kind'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
