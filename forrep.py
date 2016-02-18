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


def articles_texts(author):
    '''Функция возвращает тексты всех рецензий автора'''
    for articleLink in articles_of_author(author):
        page = url_open('http://www.rollingstone.ru'+articleLink)
        soup = BeautifulSoup(page, 'html.parser')
        yield(soup.find('div', {'class': 'block-content'}).getText())


def save_texts(author):
    '''Функция сохраняет в файлы тексты авторов'''
    number = 1
    for i in articles_texts(author):
        file = open('./articles/' + author + '_' + str(number) + '.txt', 'w', encoding='utf-8')
        file.write(i)
        file.close()
        number += 1



# Пример работы: просто пишем save_texts и id автора
#save_texts('2523')