import pickle as pkl
import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]

from sklearn.ensemble import RandomForestClassifier
CLS = RandomForestClassifier ()
CLS = CLS.fit(data,labels)
pred = CLS.predict(data)
a = accuracy_score(labels,pred)#1.0+0.9452173913043478
print(a)
f = open("classifier.pkl","wb")
pkl.dump(CLS, f)
f.close()