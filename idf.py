__author__ = 'akutinanatasha'

# пробуем гит у Наташ в пайчарм


import os,re,math
lemmas1 = set()
idf1 = {}
tf_idf1 = {}
slovar = {}
slovar_itog = {}
outfile = open('./1.csv', 'w')


for root, dirs, files in os.walk('./all'):
    for file in files:
        if file.startswith('lemma'):
            with open('./all/' + file, 'r', encoding='utf-8') as f:
                author1 = f.read()
                k = re.findall('(?<=analysis"\:\[\{"lex"\:")[а-я]+', author1)
                for i in k:
                    if i not in slovar:
                        slovar[i] = 1
                    else:
                        t = slovar[i] + 1
                        slovar[i] = t

for i in slovar:
    slovar_itog[i] = round(math.log10(586/slovar[i]),2)

for i in slovar_itog:
    outfile.write(i + ';' + str(slovar_itog[i]))
    outfile.write('\n')


outfile.close()
