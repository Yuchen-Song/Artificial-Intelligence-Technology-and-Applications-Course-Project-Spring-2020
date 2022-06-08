import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]

cls = GaussianNB()
cls = cls.fit(data, labels)
pred = cls.predict(data)
a = accuracy_score(labels,pred)
print("accuracy: ", a)#0.8192090395480226+0.81

import pickle as pkl
f = open("Bayes.pkl","wb")
pkl.dump(cls, f)
f.close()
