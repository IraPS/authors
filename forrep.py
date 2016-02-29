#  -*- coding: utf-8 -*-

# Чтобы прочитать, что делает какая-то функция, нужно напечатать, например "print(url_open.__doc__)"

import urllib.request as urlr
import re
from bs4 import BeautifulSoup
import os


def url_open(url):
    '''Функция открывает url и декодирует в utf-8'''
    urlAdress = url
    html = urlr.urlopen(urlAdress)
    html = html.read().decode('utf-8')
    return html


def count_pages(author):
    '''Функция считает количество страниц для перелистывания списка рецензий автора'''
    page = url_open('http://www.rollingstone.ru/authors/' + author)
    c = re.findall('<li><a href="/authors/' + author + '/page/.*?/">(.*?)</a>', page)
    #print(author)
    #print(c)
    return len(c)+1


def articles_links_more(author):
    '''Функция достает ссылки на рецензии автора со всех страниц'''
    for n in range(1, count_pages(author)+1):
        page = url_open('http://www.rollingstone.ru/authors/' + author + '/page/' + str(n))
        soup = BeautifulSoup(page, 'html.parser')
        for link in soup.find_all('a'):
            if 'articles/music/review' in str(link):
                yield(link.get('href'))


def articles_of_author(author):
    '''Функция возвращает массив со список ссылок на рецензии автора'''
    links = []
    for k in articles_links_more(author):
        if k not in links:
            links.append(k)
    return len(links), links


def articles_texts(author):
    '''Функция возвращает тексты всех рецензий автора'''
    new_dir = './articles/' + author
    os.makedirs(os.path.join(new_dir))
    for articleLink in articles_of_author(author)[1]:
        page = url_open('http://www.rollingstone.ru' + articleLink)
        soup = BeautifulSoup(page, 'html.parser')
        yield(soup.find('div', {'class': 'block-content'}).getText())


def save_texts(author):
    '''Функция сохраняет в файлы тексты авторов'''
    number = 1
    for i in articles_texts(author):
        file = open('./articles/' + author + '/' + str(number) + '.txt', 'w', encoding='utf-8')
        file.write(i)
        file.close()
        number += 1


def authors():
    '''Функция ищет id авторов рецензий'''
    authors = []
    articles_to_get_authors = []
    for n in range(1, 122):
        magazine = 'http://www.rollingstone.ru/music/review/page/' + str(n)
        magazine = url_open(magazine)
        soup = BeautifulSoup(magazine, 'html.parser')
        for link in soup.find_all('a'):
            if 'articles/music/review' in str(link):
                if link.get('href') not in articles_to_get_authors:
                    articles_to_get_authors.append(link.get('href'))
    for articleLink in articles_to_get_authors:
        #print('http://www.rollingstone.ru' + articleLink)
        article = url_open('http://www.rollingstone.ru' + articleLink)
        soup = BeautifulSoup(article, 'html.parser')
        span = soup.find('span', {'class': 'black-bold'})
        a1 = re.search('<a href="/authors/(.*?)/">', str(span))
        if a1 is not None:
            author = re.search('<a href="/authors/(.*?)/">', str(span)).group(1)
            if author not in authors:
                authors.append(author)
    #print(authors)
    return authors



for id in authors():
    save_texts(id)







# Пример работы: просто пишем save_texts и id автора
#save_texts('2523')