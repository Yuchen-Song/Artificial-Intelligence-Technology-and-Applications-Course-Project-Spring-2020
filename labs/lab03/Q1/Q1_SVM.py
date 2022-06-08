import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
dataset = np.loadtxt("../Lab3_data/Lab3_train.csv", delimiter=",", skiprows=1)
labels = dataset[:,0]
data = dataset[:,1:-1]
max = 0
kernel_set = ['linear','poly', 'rbf', 'sigmoid']
gamma_range = [1e-3, 1e-4]
for i in gamma_range:
    for k in kernel_set:
        cls = SVC(kernel=k, gamma=i, probability=True)
        cls = cls.fit(data, labels)
        pred = cls.predict(data)
        a = accuracy_score(labels,pred)
        if (a > max):
            max = a
            best_gamma = i
            best_kernel = k
print("accuracy: ", max)#0.79
print("best_gamma: ", best_gamma)#0.001
print("best_kernel: ", best_kernel)#linear

import pickle as pkl
f = open("Q1_SVM.pkl","wb")
pkl.dump(cls, f)
f.close()