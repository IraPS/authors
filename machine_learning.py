import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import roc_curve, auc

train = np.load('train.npz')
train = train['arr_0']
test = np.load('test.npz')
test = test['arr_0']

dc = np.load('both.npz')
dc = dc['arr_0']

clf = svm.OneClassSVM(nu=0.05)
clf.fit(train)

results = np.array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., -1.,  -1.,  -1.,  -1., -1.,  -1.]).T

# predict = clf.predict(dc) # порог выставляется автоматически

decfunc = clf.decision_function(dc)
print(list(zip(sorted(decfunc),sorted(results))))

# порог вставляется вручную, на основе результатов decision function
predict = []
for i in decfunc:
    if i < -0.02:
        predict.append(-1.)
    else:
        predict.append(1.)

print('accuracy of predict', (predict == results).mean())

fpr, tpr, _ = roc_curve(results, decfunc)
roc_auc = auc(fpr, tpr)
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()
