__author__ = 'IrinaPavlova'
#  -*- coding: utf-8 -*-
#from main import main
import re, codecs, os


def texttag(text):
    textt = '<div rend="section" xml:id=(.*?)>'
    res = re.search(textt, text)
    if res is not None:
        texttn = '<text xml:id=' + res.group(1) + '>' + '\n\t<body>\n\t\t<opener>'
        text = re.sub(textt, texttn, text)
    return text


def adr(text):
    addresseet = re.compile('<head rend=".+">\n\s*<hi>(.*?[0-9]+)?(.*?)</hi>\n')
    addressee = re.search(addresseet, text)
    if addressee is not None:
        addresseetn = '<hi>' + addressee.group(1) + '<persName role="addressee" type="person">' + addressee.group(2) + '</persName></hi>'
        text = re.sub(addresseet, addresseetn, text)
    return text


def data(text):
    d = '(<p rend="Data left">)(.*?)</p>'
    res = re.search(d, text, re.DOTALL)
    if res is not None:
        text = re.sub('<p rend="Data left">\n*\t*.*?\n*\t*</p>', '<DATE>' + res.group(2) + '</date>', text)
    return text


def salute_beg(text):
    salutet = '<p rend="Obrashenie.*?">(.*?)</p>'
    salute = re.findall(salutet, text, re.DOTALL)
    print(len(salute))
    if len(salute) is not 0:
        # print(salute)
        if len(salute) > 1:
            for i in range(len(salute)-1):
                text = re.sub('<p rend="Obrashenie.*?">' + salute[i] + '</p>', '', text)
        salute = ''.join(salute)
        # print(salute)
        salutetn = '<salute>' + salute + '</salute>\r\n\t\t</opener>\r\n'
        text = re.sub('<p rend="Obrashenie.*?">\n*\t*(.*?)\n*\t*</p>', salutetn, text)
    else:
        text = re.sub('</date>', '</date>\n\t\t</opener>', text)
    return text


def half(text):
    splitted = text.split('<p rend="Textpetit_otstup left">')
    half1 = splitted[0]
    return half1


def salute_end(text, lines):
    # text = re.sub(u'<p rend="right">([^0-9]*?)</p>', '<signed rend ="right">\\1</signed>', text)
    lineshalf = len(lines)//2
    needed = lines[lineshalf:]
    needed0 = ''.join(needed)
    # print(needed0)
    needed = ''.join(needed)
    salutet = '<p rend="right">([^0-9]*?)</p>'
    salute = re.findall(salutet, needed, re.DOTALL)
    if salute is not None:
        # print(salute)
        '''
        if len(salute) > 1:
            for i in range(len(salute)-1):
                needed = re.sub('<p rend="right">' + salute[i] + '</p>', '', needed)
                '''
        if len(salute) > 1:
            print(salute)
            needed = re.sub('<p rend="right">' + salute[0] + '</p>', '<closer><signed rend="right">' + salute[0] + '</signed>', needed)
            for i in range(1, len(salute)-2):
                needed = re.sub('<p rend="right">' + salute[i] + '</p>', '<signed rend="right">' + salute[i] + '</signed>', needed)
            needed = re.sub('<p rend="right">' + salute[-1] + '</p>', '<signed rend="right">' + salute[-1] + '</signed></closer>', needed)
        # salute = ''.join(salute)
        # print(salute)
        # salutetn = '<closer><signed rend="right">' + salute + '</signed></closer>'
        # needed = re.sub('<p rend="right">\n*\t*(.*?)\n*\t*</p>', salutetn, needed)
        # print(needed)
        # print(needed)
        text = text.replace(needed0, needed)
    return text



def se(text, lines):
    lineshalf = len(lines)//2
    needed = lines[lineshalf:]
    needed0 = ''.join(needed)
    # print(needed0)
    needed = ''.join(needed)
    needed = re.sub(u'(<p rend="right">)([^0-9]*?)(</p>)', u'<closer><signed rend="right">\\2</signed></closer>', needed)
    text = text.replace(needed0, needed)
    return text


def notes(text):
    check = re.search('<p rend="Textpetit_otstup left">\n\t', text)
    if check is not None:
        allnotes = text.split('<p rend="Textpetit_otstup left">\n\t')[1]
        notet = '<hi>\n*\t*[0-9]+\n*\t*</hi>(.*?)</p>'
        note = re.findall(notet, allnotes, re.DOTALL)
        arr = ['']
        if note is not None:
            for i in note:
                arr.append(i)
            for n in range(1, len(arr)):
                text = re.sub('<hi>'+str(n)+'</hi>', '<note xml:id="note' + str(n) + '" resp="volume_editor">' + arr[n] + '</note>', text, re.DOTALL)
    return text


def findel(text): # ВОТ ЗДЕСЬ НУЖНО УДАЛЯТЬ ТО, ЧТО ПОСЛЕ ТЕКСТА ПИСЬМА И ДОПИСЫВАТЬ ЗАКРЫВАЮЩИЕ ТЕГИ, НО для
    # для хедера эта инфа нужна, можно удалить после запуска хедера
    pass

for root, dirs, files in os.walk('./'):
    for name in files:
        if not name.startswith('.DS'):
            if name.endswith('out.xml'):
                print(name)
                to_read = name
                to_write = name + '_tagged.xml'
                # os.chdir('./splitted_letters')

                text_r = codecs.open(to_read, 'r', 'utf-8')
                # os.chdir('./tagged')
                text_w = codecs.open(to_write, 'w', 'utf-8')
                t = text_r.read()

                textr = codecs.open(to_read, 'r', 'utf-8')
                lines = []
                for i in textr: lines.append(i)
                textr.close()

                for e in lines:
                    if '</teiHeader>' in e:
                        ind1 = lines.index(e)
                    if '<p rend="Textpetit_otstup left">' in e:
                        ind2 = lines.index(e)

                letterlines = lines[ind1:ind2]


                t1 = texttag(t)
                # t1 = salute_end(t1, letterlines)
                t1 = se(t1, letterlines)
                t1 = adr(t1)
                t1 = data(t1)
                t1 = notes(t1)
                t1 = t1.split('\t\t\t\t\t\t<p rend="Textpetit_otstup left">')[0]
                t1 = salute_beg(t1)


                t1 = re.sub('\n*\t*</head>', '', t1)



                text_w.write(t1)
                text_w.write('\t</body>\n</text>\n</TEI>')


                text_r.close()
                text_w.close()