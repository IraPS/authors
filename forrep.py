#  -*- coding: utf-8 -*-

# Чтобы прочитать, что делает какая-то функция, нужно напечатать, например "print(url_open.__doc__)"

import urllib.request as urlr
import re
from bs4 import BeautifulSoup


def url_open(url):
    '''Функция открывает url и декодирует в utf-8'''
    urlAdress = url
    html = urlr.urlopen(urlAdress)
    html = html.read().decode('utf-8')
    return html


def articles_links(author):
    '''Функция достает ссылки на рецензии автора с его первой страницы'''
    page = url_open('http://www.rollingstone.ru/authors/' + author)
    soup = BeautifulSoup(page, 'html.parser')
    for link in soup.find_all('a'):
        if 'articles/music/review' in str(link):
            yield(link.get('href'))


def count_pages(author):
    '''Функция считает количество страниц для перелистывания списка рецензий автора'''
    page = url_open('http://www.rollingstone.ru/authors/' + author)
    c = re.findall('<li><a href="/authors/' + author + '/page/.*?/">(.*?)</a>', page)
    return c


def articles_links_more(author):
    '''Функция достает ссылки на рецензии автора с последующих страниц'''
    for n in count_pages(author):
        page = url_open('http://www.rollingstone.ru/authors/' + author + '/page/' + n)
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('a'):
            if 'articles/music/review' in str(link):
                yield(link.get('href'))



def articles_of_author(author):
    '''Функция возвращает массив со список ссылок на рецензии автора'''
    links = []
    for i in articles_links(author):
        if i not in links:
            links.append(i)
    for k in articles_links_more(author):
        if k not in links:
            links.append(k)
    return links


print(len(articles_of_author('2523')), articles_of_author('2523'))


