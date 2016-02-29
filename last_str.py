import os

for root, dirs, files in os.walk('./articles1'):
    for file in files:
        if file.endswith('.txt'):
            f = open('./articles1/' + file, 'r', encoding='utf-8')
            f0 = f.readlines()
            f1 = list()
            f1.append(f0[:-1])
            f.close()
            f = open('./articles1/' + file + '_new.txt', 'w', encoding='utf-8')
            for i in f1:
                for u in i:
                    f.write(u)
            f.close()