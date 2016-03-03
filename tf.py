__author__ = 'akutinanatasha'

import os,re,math
corpus1 = []
mass = {} #делить на кол-во слов в документе


"""
def lemmas(file):
    os.system('/Users/akutinanatasha/Desktop/Python/module4/artic/' + 'mystem -d -n -i -s --format=json --eng-gr ' + '/Users/akutinanatasha/Desktop/Python/module4/artic/763_54/' + file + ' ' + '/Users/akutinanatasha/Desktop/Python/module4/artic/763_54/' + 'lemma' + file)

for root, dirs, files in os.walk('./763_54'):
    for file in files:
        if file.endswith('.txt'):
            lemmas(file)
"""

#предлоги можно еще считать?

def pril(sent):  #12
    k = re.findall('analysis.*?gr.*?(A)[^P|^D|^N]', sent)
    return(len(k))

def nar(sent): #1
    k = re.findall('analysis.*?gr.*?(ADV|ADVPRO)', sent)
    return(len(k))

def chispril(sent): #0
    k = re.findall('analysis.*?gr.*?(ANUM)', sent)
    return(len(k))

def mestpril(sent): #1
    k = re.findall('analysis.*?gr.*?(APRO)', sent)
    return(len(k))

def chkomp(sent): #0
    k = re.findall('analysis.*?gr.*?(COM)', sent)
    return(len(k))

def sojuz(sent): #2
    k = re.findall('analysis.*?gr.*?(CONJ)', sent)
    return(len(k))

def intj(sent): #0
    k = re.findall('analysis.*?gr.*?(INTJ)', sent)
    return(len(k))

def num(sent): #0
    k = re.findall('analysis.*?gr.*?[^A](NUM)', sent)
    return(len(k))

def part(sent): #2
    k = re.findall('analysis.*?gr.*?(PART)', sent)
    return(len(k))

def predl(sent): #5
    k = re.findall('analysis.*?gr.*?[^ADV|^A](PR)[^O]', sent)
    return(len(k))

def sush(sent): #17
    k = re.findall('analysis.*?gr.*?(S)[^P]', sent)
    return(len(k))

def glag(sent): #4
    k = re.findall('analysis.*?gr.*?[^D](V)[^P]', sent)
    return(len(k))

def mestsush(sent): #0
    k = re.findall('analysis.*?gr.*?(SPRO)', sent)
    return(len(k))

def tfidf(i, col):
    infile = open('./1.csv', 'r')
    for j in infile:
        j = j.split(';')
        if i == j[0]:
            idf = j[1].strip()
            idf = float(idf)
    return(round(((mass[i]/col)*idf), 3)) #col - кол-во слов в документе


ids = ['1830_36', '141_70', '103_95', '2510_49', '2523_63', '53_50', '557_71', '6_100', '763_54']
for x in ids:
    outfile = open('./' + x + '.csv', 'w')
    for root, dirs, files in os.walk('./' + x):
        for file in files:
            if file.startswith('lemma'):
                with open('./' + x + '/' + file, 'r', encoding='utf-8') as f:
                    author1 = f.read()
                    k2 = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', author1) #кол-во слов в документе
                    a_texts = re.split(r'text.+\\s"}', author1)
                    for i in k2:
                        if i not in mass:
                            mass[i] = 1
                        else:
                            s = mass[i] + 1
                            mass[i] = s
                    for p in a_texts: ###
                        cor = []
                        n = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', p)
                        infile = open('./1.csv', 'r')
                        for j in infile:
                            j = j.strip()
                            j = j.split(';')
                            for k in n:
                                if k == j[0]:
                                    cor.append(tfidf(k, len(k2)))
                                else:
                                    cor.append(0)
                        b = [pril(p), nar(p), chispril(p), mestpril(p), chkomp(p), sojuz(p), intj(p), num(p),
                             part(p), predl(p), sush(p), glag(p), mestsush(p)]
                        for i in b:
                            cor.append(i)
                        corpus1.append(cor)
                        for i in cor:
                            i = str(i)
                            outfile.write(i + ', ')
                        outfile.write('\n')
                #print(p)
            #print(mass)
            mass = {}

#print(k)
#print(corpus1)

outfile.close()



