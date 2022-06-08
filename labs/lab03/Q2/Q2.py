import pickle as pkl
f = open("../Q1/Q1_DT.pkl", "rb")
clsDT = pkl.load(f)
f.close()

f = open("../Q1/Q1_k-nn.pkl", "rb")
clsKNN = pkl.load(f)
f.close()

f = open("../Q1/Q1_SVM.pkl", "rb")
clsSVM = pkl.load(f)
f.close()

f = open("../Q1/Q1_MLP.pkl", "rb")
clsMLP = pkl.load(f)
f.close()

import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../Lab3_data/Lab3_train.csv", delimiter=",", skiprows=1)
labels = dataset[:,0]
data = dataset[:,1:-1]

from sklearn.ensemble import VotingClassifier
voting = VotingClassifier (estimators=[('DT',clsDT),('KNN',clsKNN),('MLP',clsMLP),('SVM',clsSVM)], voting='soft')
voting = voting.fit(data,labels)
pred = voting.predict(data)
a = accuracy_score(labels,pred)#hard:0.765 soft:0.9275

f = open("Q2_classifier.pkl","wb")
pkl.dump(voting, f)
f.close()