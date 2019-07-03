import requests
from bs4 import BeautifulSoup as bs


gamenews_url = 'https://www.igromania.ru/tech/articles/'


def igromania_parse(gamenews_url):
    request = requests.get(gamenews_url)
    soup = bs(request.content, 'html.parser')
    print(soup)

igromania_parse(gamenews_url)




