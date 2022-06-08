import pickle as pkl
j = []
for i in range(201):
    if i % 8 == 1 or i % 8 == 3 or i % 8 == 4 or i % 8 == 6 or i % 8 == 7:
        j.append(1)
    else:
        j.append(0)

answers = {'Q2_i': 'A', 'Q2_ii': j}
f = open('Q2.pkl', 'wb')
pkl.dump(answers, f)
f.close()