import pickle as pkl

answer = {'Q2':
              [
                  ("mean",0.9275),
                  ("max",0.76375)
              ]
          }

f = open('Q2.pkl', 'wb')
pkl.dump(answer, f)
f.close()
