import pickle as pkl

answer = {'Q1':
              [("k-nn", {"n_neighbors": 3}, 0.83125),
               ("DT", {"max_depth": 7}, 0.85125),
               ("SVM", {"kernel": "linear", "gamma": 0.001}, 0.79),
               ("MLP", {"activation": "logistic", "solver": "adam"}, 0.97)]
          }

f = open('Q1.pkl', 'wb')
pkl.dump(answer, f)
f.close()
