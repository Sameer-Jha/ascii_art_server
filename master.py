import requests
from bs4 import BeautifulSoup as bs
from Catalogue import catalogue
from random import choice

def link_gen():
    base_url = 'https://www.asciiart.eu/'
    category = choice(list(catalogue.keys()))
    sub_category = choice(catalogue[category])
    url = f'{base_url}{category}{sub_category}'
    return url

def ascii_print():
    ascii_page = requests.get(link_gen()).content
    ascii_parse = bs(ascii_page, 'html.parser')
    ascii_arts_g = ascii_parse.find_all('pre')
    ascii_arts = [art for art in ascii_arts_g]
    try:
        print(ascii_arts[1].get_text()+"\n")
        ascii_arts.pop(1)
    except IndexError:
        ascii_print()
        return None
    art = choice(ascii_arts)
    print(art.get_text())


    


