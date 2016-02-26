__author__ = 'akutinanatasha'

import os,re,math
lemmas1 = set()
idf1 = {}
tf_idf1 = {}
corpus1 = []
mass = {} #делаить на кол-во слов в документе

"""
def lemmas(file):
    os.system('/Users/akutinanatasha/Desktop/Python/module4/artic/' + 'mystem -d -n -i -s --format=json --eng-gr ' + '/Users/akutinanatasha/Desktop/Python/module4/artic/784/' + file + ' ' + '/Users/akutinanatasha/Desktop/Python/module4/artic/784/' + 'lemma' + file)

for root, dirs, files in os.walk('./784'):
    for file in files:
        if file.endswith('.txt'):
            lemmas(file)
"""

#предлоги можно еще считать?

def pril(sent):
    k = re.findall('analysis.*?gr.*?(A|ANUM)[^P]', sent)
    return(len(k))

def sush(sent):
    k = re.findall('analysis.*?gr.*?(S)[^P]', sent)
    return(len(k))

def glag(sent):
    k = re.findall('analysis.*?gr.*?(V)[^P]', sent)
    return(len(k))

def nar(sent):
    k = re.findall('analysis.*?gr.*?(ADV|ADVPRO)[^P]}', sent)
    return(len(k))

def mest(sent):
    k = re.findall('analysis.*?gr.*?(SPRO)[^P]', sent)
    return(len(k))

def tfidf(i):
    infile = open('./1.csv', 'r')
    for j in infile:
        j = j.split(';')
        if i == j[0]:
            idf = j[1].strip()
    return(mass[i]*idf) #формула?


for root, dirs, files in os.walk('./1830'):
    for file in files:
        if file.startswith('lemma'):
            with open('./1830/' + file, 'r', encoding='utf-8') as f:
                author1 = f.read()
                a_texts = re.split(r'text.+\\s"}', author1)
                k = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', author1) #повторы?
                for i in k:
                    if i not in mass:
                        mass[i] = 1
                    else:
                        s = mass[i] + 1
                        mass[i] = s
                for p in a_texts:
                    k = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', p)
                    for p in k:
                        corpus1.append(tfidf(p))
                    corpus1.append([[pril(i), sush(i), glag(i), nar(i), mest(i)] for i in a_texts])
        mass = {}
#print(k)
print(corpus1)




