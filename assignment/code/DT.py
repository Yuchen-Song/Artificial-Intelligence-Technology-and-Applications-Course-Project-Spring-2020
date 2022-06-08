import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import tree
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]
for i in range(1,100):
    i += 1
    cls = tree.DecisionTreeClassifier(max_depth=i)
    cls = cls.fit(data, labels)
    pred = cls.predict(data)
    a = accuracy_score(labels,pred)
    if (a > 0.85):
        max = a
        best = i
        break
print("accuracy: ", max)#0.8691873098652759+0.8617391304347826
print("best: ", best)#2

import pickle as pkl
f = open("DT.pkl","wb")
pkl.dump(cls, f)
f.close()
