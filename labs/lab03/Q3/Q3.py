import pickle as pkl
f = open("../Q2/Q2_classifier.pkl", "rb")
cls = pkl.load(f)
f.close()

import numpy as np
from sklearn.metrics import accuracy_score
dataset = np.loadtxt("../Lab3_data/Lab3_test.csv", delimiter=",", skiprows=1)
data = dataset[:,1:]
pred = cls.predict(data)
answer = {'Q3':pred}
f = open('Q3.pkl','wb')
pkl.dump(answer,f)
f.close()