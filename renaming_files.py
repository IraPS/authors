__author__ = 'IrinaPavlova'
import os

for root, dirs, files in os.walk('./articles'):
    for dir in dirs:
        print(dir)
        for root, dirs, files in os.walk('./articles/' + dir):
            for file in files:
                #print(file)
                if file.endswith('.txt'):
                    print(file)
                    f = open('./articles/' + dir + '/' + file, 'r', encoding='utf-8')
                    t = f.read()
                    print('yes')
                    f.close()
                    f = open('./articles/' + dir + '/' + dir + '_' + file, 'w', encoding='utf-8')
                    f.write(t)
                    f.close()