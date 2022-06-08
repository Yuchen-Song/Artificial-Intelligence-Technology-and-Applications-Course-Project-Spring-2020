import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
dataset = np.loadtxt("../Lab3_data/Lab3_train.csv", delimiter=",", skiprows=1)
labels = dataset[:,0]
data = dataset[:,1:-1]
max = 0
for i in range(2,10):
    i += 1
    cls = KNeighborsClassifier(n_neighbors=i)
    cls = cls.fit(data, labels)
    pred = cls.predict(data)
    a = accuracy_score(labels,pred)
    if (a > max):
        max = a
        best = i
print("accuracy: ", max)#0.83125
print("best: ", best)#3

import pickle as pkl
f = open("Q1_k-nn.pkl","wb")
pkl.dump(cls, f)
f.close()