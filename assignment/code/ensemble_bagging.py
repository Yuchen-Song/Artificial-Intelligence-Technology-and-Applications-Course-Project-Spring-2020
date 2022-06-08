import pickle as pkl
import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]

from sklearn.ensemble import BaggingClassifier
CLS = BaggingClassifier ()
CLS = CLS.fit(data,labels)
pred = CLS.predict(data)
a = accuracy_score(labels,pred)#0.9943502824858758+0.9247826086956522
print(a)
f = open("classifier.pkl","wb")
pkl.dump(CLS, f)
f.close()