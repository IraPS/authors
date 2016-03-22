import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from scipy import sparse
from sklearn.metrics import roc_curve, auc

train1830 = np.load('author1830_36-2.npz')
train1830 = train1830['arr_0']
test1830 = np.load('test1830.npz')
test1830 = test1830['arr_0']

train6 = np.load('author2523_63_final.npz')
train6 = train6['arr_0']
test6 = np.load('test_author557_final.npz')
test6 = test6['arr_0']

test103 = np.load('test103.npz')
test103 = test103['arr_0']

clf = svm.OneClassSVM(nu=0.05)
clf.fit(train6)

predict = clf.predict(test6)
a = 0
print(predict)
for i in predict:
    if i == -1:
        a += 1
print((len(predict)-a)/len(predict))

decfunc = clf.decision_function(test1830)
#print(decfunc)

results = np.array([[float(1)]*len(test1830)]).T
#print(results)

fpr, tpr, _ = roc_curve(results, decfunc)
#print(fpr, tpr)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
#plt.show()
