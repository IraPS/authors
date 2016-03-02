import os
for root, dirs, files in os.walk('./articles'):
    for dir in dirs:
        print(dir)
        for root, dirs, files in os.walk('./articles/' + dir):
            for file in files:
                if file.endswith('.txt'):
                    f = open('./articles/' + dir + '/' + file, 'r', encoding='utf-8')
                    f0 = f.readlines()
                    f1 = list()
                    if 'Apple' in f0[-1] or 'iTunes' in f0[-1] or 'Deezer' in f0[-1]:
                        print(f0[-1])
                        f1.append(f0[:-1])
                    else:
                        f1.append(f0)

                    #print(f1)
                    f.close()
                    f = open('./articles/' + dir + '/' + file[:-4] + '_new.txt', 'w', encoding='utf-8')
                    for i in f1:
                        for u in i:
                            f.write(u)
                    f.close()
