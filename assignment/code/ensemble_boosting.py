import pickle as pkl
import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]

from sklearn.ensemble import GradientBoostingClassifier
CLS = GradientBoostingClassifier ()
CLS = CLS.fit(data,labels)
pred = CLS.predict(data)
a = accuracy_score(labels,pred)#0.9730551933941765+0.9365217391304348
print(a)
f = open("classifier.pkl","wb")
pkl.dump(CLS, f)
f.close()