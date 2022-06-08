import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]
activation_set = ['identity','logistic','tanh','relu']
solver_set = ['lbfgs','sgd','adam']
for s in solver_set:
    for k in activation_set:
        cls = MLPClassifier(activation=k,max_iter=10000,solver=s)
        cls = cls.fit(data, labels)
        pred = cls.predict(data)
        a = accuracy_score(labels,pred)
        if (a > 0.85):
            max = a
            best_solver = s
            best_activation = k
            break
print("accuracy: ", max)#0.9104737070838765+0.8969565217391304
print("best_solver: ", best_solver)#adam
print("best_activation: ", best_activation)#identity

import pickle as pkl
f = open("MLP.pkl","wb")
pkl.dump(cls, f)
f.close()