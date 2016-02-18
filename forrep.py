#  -*- coding: utf-8 -*-

import urllib.request as urlr
import re
from bs4 import BeautifulSoup


def url_open(url):
    urlAdress = url
    html = urlr.urlopen(urlAdress)
    html = html.read().decode('utf-8')
    return html


def articles_links(author):
    page = url_open('http://www.rollingstone.ru/authors/' + author)
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.find_all('a'):
        if 'articles/music/review' in str(link):
            yield(link.get('href'))


def count_pages(author):
    page = url_open('http://www.rollingstone.ru/authors/' + author)
    c = re.findall('<li><a href="/authors/6/page/.*?/">(.*?)</a>', page)
    return c


def articles_links_more(author):
    for n in count_pages(author):
        page = url_open('http://www.rollingstone.ru/authors/' + author + '/page/' + n)
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('a'):
            if 'articles/music/review' in str(link):
                yield(link.get('href'))


links_6 = []

for i in articles_links('6'):
    if i not in links_6:
        links_6.append(i)
for i in articles_links_more('6'):
    if i not in links_6:
        links_6.append(i)

print(len(links_6), links_6)

