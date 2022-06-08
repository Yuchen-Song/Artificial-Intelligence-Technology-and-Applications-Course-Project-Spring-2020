import pickle as pkl
f = open("classifier.pkl", "rb")
cls = pkl.load(f)
f.close()

import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[1::2,57]
data = dataset[1::2,0:-1]
pred = cls.predict(data)
a = accuracy_score(labels,pred)
print("accuracy: ")
print(a)#0.9443478260869566
from sklearn.metrics import f1_score
f1 = f1_score(labels,pred)
print("f1: ")
print(f1)
from sklearn.metrics import average_precision_score
p = average_precision_score(labels,pred)
print("precision: ")
print(p)