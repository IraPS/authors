__author__ = 'akutinanatasha'

import os,re,math
lemmas1 = set()
idf1 = {}
tf_idf1 = {}
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
            idf = float(idf)
    return(round((mass[i]*idf), 2)) #формула?


ids = ['103_95', '141_70', '1830_36', '2510_49', '2523_63', '53_50', '557_71', '6_100', '763_54']
for x in ids:
    outfile = open('./' + x + '.csv', 'w')
    for root, dirs, files in os.walk('./' + x):
        for file in files:
            if file.startswith('lemma'):
                with open('./' + x + '/' + file, 'r', encoding='utf-8') as f:
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
                        cor = []
                        n = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', p)
                        infile = open('./1.csv', 'r')
                        for j in infile:
                            j = j.strip()
                            j = j.split(';')
                            for k in n:
                                if k == j[0]:
                                    cor.append(tfidf(k))
                                else:
                                    cor.append(0)
                        cor.append(pril(p))
                        cor.append(sush(p))
                        cor.append(glag(p))
                        cor.append(nar(p))
                        cor.append(mest(p))
                        corpus1.append(cor)
                        for i in cor:
                            i = str(i)
                            outfile.write(i + ', ')
                        outfile.write('\n')
            mass = {}

#print(k)
#print(corpus1)

outfile.close()



