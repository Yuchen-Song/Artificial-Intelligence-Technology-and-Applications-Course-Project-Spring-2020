import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import tree
dataset = np.loadtxt("../Lab3_data/Lab3_train.csv", delimiter=",", skiprows=1)
labels = dataset[:,0]
data = dataset[:,1:-1]
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
print("accuracy: ", max)#0.85125
print("best: ", best)#7

import pickle as pkl
f = open("Q1_DT.pkl","wb")
pkl.dump(cls, f)
f.close()
