__author__ = 'akutinanatasha'

import os,re
import numpy
mass = {}


"""
def lemmas(file):
    os.system('/Users/akutinanatasha/Desktop/Python/module4/artic/' + 'mystem -d -n -i -s --format=json --eng-gr ' + '/Users/akutinanatasha/Desktop/Python/module4/artic/тест/' + file + ' ' + '/Users/akutinanatasha/Desktop/Python/module4/artic/тест/' + 'lemma' + file)

for root, dirs, files in os.walk('./тест'):
    for file in files:
        if file.endswith('.txt'):
            lemmas(file)
"""

def pril(sent):
    k = re.findall('analysis.*?gr.*?(A)[^P|^D|^N]', sent)
    return(len(k))

def nar(sent):
    k = re.findall('analysis.*?gr.*?(ADV|ADVPRO)', sent)
    return(len(k))

def chispril(sent):
    k = re.findall('analysis.*?gr.*?(ANUM)', sent)
    return(len(k))

def mestpril(sent):
    k = re.findall('analysis.*?gr.*?(APRO)', sent)
    return(len(k))

def chkomp(sent):
    k = re.findall('analysis.*?gr.*?(COM)', sent)
    return(len(k))

def sojuz(sent):
    k = re.findall('analysis.*?gr.*?(CONJ)', sent)
    return(len(k))

def intj(sent):
    k = re.findall('analysis.*?gr.*?(INTJ)', sent)
    return(len(k))

def num(sent):
    k = re.findall('analysis.*?gr.*?[^A](NUM)', sent)
    return(len(k))

def part(sent):
    k = re.findall('analysis.*?gr.*?(PART)', sent)
    return(len(k))

def predl(sent):
    k = re.findall('analysis.*?gr.*?[^ADV|^A](PR)[^O]', sent)
    return(len(k))

def sush(sent):
    k = re.findall('analysis.*?gr.*?(S)[^P]', sent)
    return(len(k))

def glag(sent):
    k = re.findall('analysis.*?gr.*?[^D](V)[^P]', sent)
    return(len(k))

def mestsush(sent):
    k = re.findall('analysis.*?gr.*?(SPRO)', sent)
    return(len(k))

def tfidf(i, col):
    infile = open('./1.csv', 'r')
    for j in infile:
        j = j.split(';')
        if i == j[0]:
            idf = j[1].strip()
            idf = float(idf)
    return(round(((mass[i]/col)*idf), 3))


ids = ['103', '141', '1830', '2510', '2523', '53', '557', '6', '763']
for x in ids:
    a = []
    id1 = int(x.split('_')[0])
    print(x)
    for root, dirs, files in os.walk('./тест/' + x):
        for file in files:
            if file.startswith('lemma'):
                print(file)
                with open('./тест/' + x + '/' + file, 'r', encoding='utf-8') as f:
                    author1 = f.read()
                    cor = []
                    k2 = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', author1) #кол-во слов в документе
                    for i in k2:
                        if i not in mass:
                            mass[i] = 1
                        else:
                            s = mass[i] + 1
                            mass[i] = s
                    infile = open('./1.csv', 'r')
                    for j in infile:
                        j = j.strip()
                        j = j.split(';')
                        if j[0] in k2:
                            #print('da')
                            cor.append(tfidf(j[0], len(k2)))
                        else:
                            cor.append(0)
                    b = [pril(author1), nar(author1), chispril(author1), mestpril(author1), chkomp(author1), sojuz(author1), intj(author1), num(author1),
                             part(author1), predl(author1), sush(author1), glag(author1), mestsush(author1)]
                    for i in b:
                        cor.append(i)
                    a.append(cor)
                    cor = []
            mass = {}
        print(len(a))
        a = numpy.array(a)
        print(x)
        numpy.savez_compressed('test_author' + x + '_final.npz', a)
        #a = []



