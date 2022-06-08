import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
dataset = np.loadtxt("../Lab3_data/Lab3_train.csv", delimiter=",", skiprows=1)
labels = dataset[:,0]
data = dataset[:,1:-1]
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
print("accuracy: ", max)#0.97
print("best_solver: ", best_solver)#adam
print("best_activation: ", best_activation)#logistic

import pickle as pkl
f = open("Q1_MLP.pkl","wb")
pkl.dump(cls, f)
f.close()