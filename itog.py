__author__ = 'akutinanatasha'

import os,re,math
from sklearn import svm
from sklearn import grid_search

mass_ids = []
mass_ob = []
ids = ['1830_36', '141_70', '103_95', '2510_49', '2523_63', '53_50', '557_71', '6_100', '763_54']
for x in ids:
    print(x)
    infile = open('./' + x + '.csv', 'r')
    infile = infile.read()
    infile = infile.split('\n')
    id2 = (len(infile))
    mass_ids_one = [int(x.split('_')[0]) for i in range(id2)]
    for l in mass_ids_one:
        mass_ids.append(l)
    for i in infile:
        i = i.split(', ')
        one = [j for j in i]
        mass_ob.append(one)

print(mass_ob)
print(mass_ids)
parameters = {'C' : (.1, .5, 1.0, 2.5, 2.0)}
gs = grid_search.GridSearchCV(svm.LinearSVC(), parameters)
gs.fit(mass_ob, mass_ids)
print(gs.best_score_)
print(gs.best_estimator_)



