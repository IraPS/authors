#  -*- coding: utf-8 -*-

import urllib.request as urlr
import re
from bs4 import BeautifulSoup


def do(url):
    urlAdress = url
    html = urlr.urlopen(urlAdress)
    html = html.read().decode('utf-8')
    return(html)


author = '2523/'
authorurl = 'http://www.rollingstone.ru/authors/' + author
res = do(authorurl)

soup = BeautifulSoup(res, 'html.parser')
for link in soup.find_all('a'):
    if 'articles/music/review' in str(link):
        print(link.get('href'))

