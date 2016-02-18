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
links = re.findall('<span class="href-more">\|<a href="/articles(.*?)">', res)
#for i in links:
    #print('YES')
    #print(do('http://www.rollingstone.ru'+i))

soup = BeautifulSoup(res, 'html.parser')
print(soup.prettify())

