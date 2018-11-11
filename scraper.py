import requests
from bs4 import BeautifulSoup
BASE_URL = 'http://kkc.or.kr/megazine/megazine_02_view.html?idx=3&page=1&key='
response = requests.get(BASE_URL)

print(response.status_code)
dom = BeautifulSoup(response.content, "html.parser")
post_elements = dom.select('div.kind')

print(post_elements)

'''
# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get()
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'div.kind'
    )

data = {}

for title in my_titles:
    data[title.text] = title.get('href')

with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
a = json.dumps(data)
print(data)
print(type(data))
print(a)
print(type(a))
print(chardet.detect(a))
'''
