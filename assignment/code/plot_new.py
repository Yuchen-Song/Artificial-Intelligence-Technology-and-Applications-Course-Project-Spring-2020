import matplotlib.pyplot as plt
import numpy as np
dataset = np.loadtxt("../spamBase/spambase.data", delimiter=",")
labels = dataset[0::2,57]
data = dataset[0::2,0:-1]

X = data[:906,1] #data for spams(label = 1)
Y = data[:906,53]
plt.scatter(X, Y, c='y', marker='.', label='spams')

X = data[907:,1] #data for nonspams(label = 1)
Y = data[907:,53]
plt.scatter(X, Y, c='c', marker='.', label='normal')
plt.xlabel('total capital letters')
plt.ylabel('longest all-captital letter')
plt.legend()
plt.show()
#54,55
