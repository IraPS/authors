#  -*- coding: utf-8 -*-

import urllib.request as urlr
import re

urlAdress = 'http://www.rollingstone.ru/authors/2523/'
html = urlr.urlopen(urlAdress)
html = html.read().decode('utf-8')
print(type(html))
