import minimax
import pickle as pkl
sg = [0 for i in range(201)]
son = [[],[1-1],[2-1],[3-1],[4-1,4-4],[5-1,5-4],[6-1,6-4]]
for j in range(7,201):
    son.append([j-1,j-4,j-7])
minimax.SG(sg, son)

answers = {'Q2_i': 'A', 'Q2_ii': sg}
f = open('Q2.pkl', 'wb')
pkl.dump(answers, f)
f.close()