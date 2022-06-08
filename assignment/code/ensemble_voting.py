import pickle as pkl
f = open("DT.pkl", "rb")
clsDT = pkl.load(f)
f.close()

f = open("k-nn.pkl", "rb")
clsKNN = pkl.load(f)
f.close()

f = open("MLP.pkl", "rb")
clsMLP = pkl.load(f)
f.close()

f = open("Bayes.pkl", "rb")
clsBayes = pkl.load(f)
f.close()

import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]

from sklearn.ensemble import VotingClassifier
voting = VotingClassifier (estimators=[('DT',clsDT),('KNN',clsKNN),('MLP',clsMLP),('Bayes',clsBayes)], voting='soft')
voting = voting.fit(data,labels)
pred = voting.predict(data)
a = accuracy_score(labels,pred)#hard:0.9091699261190787 soft:0.930465015210778
print(a)
f = open("classifier.pkl","wb")
pkl.dump(voting, f)
f.close()