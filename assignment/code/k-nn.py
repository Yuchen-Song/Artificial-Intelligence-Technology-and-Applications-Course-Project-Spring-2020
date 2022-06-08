import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]
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
print("accuracy: ", max)#0.8857018687527162+0.7517391304347826
print("best: ", best)#3

import pickle as pkl
f = open("k-nn.pkl","wb")
pkl.dump(cls, f)
f.close()