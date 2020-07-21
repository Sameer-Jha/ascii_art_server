import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.asciiart.eu/'

categories = []

page = requests.get(url).content

parse = bs(page, 'html.parser')

categories = [c['href'] for c in parse.select('.directory-columns ul li a')]

catalogue = {}

for category in categories:
    print(category)
    sub_url = url+category
    sub_page = requests.get(sub_url).content
    subparse = bs(sub_page, 'html.parser')
    catalogue[category] = [c['href'] for c in subparse.select('.directory-columns ul li a')]

print(catalogue)
ascii_page_url = url+categories[0]+catalogue[categories[0]][2]
ascii_page = requests.get(ascii_page_url).content
ascii_parse = bs(ascii_page, 'html.parser')
ascii_arts = ascii_parse.find_all('pre')
for art in ascii_arts:
    print(art.get_text())


