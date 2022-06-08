import pickle as pkl

# Q1
f = open('Q1.pkl', 'rb')
answers = pkl.load(f)
f.close()
Q1 = answers

# Q2
f = open('Q2.pkl', 'rb')
answers = pkl.load(f)
f.close()
Q2_i = answers['Q2_i']
Q2_ii = answers['Q2_ii']

# Q3
f = open('Q3.pkl', 'rb')
answers = pkl.load(f)
f.close()
Q3_i = answers['Q3_i']
Q3_ii = answers['Q3_ii']

# write the answer to final pickle file
answer = {'Q1': Q1, 'Q2_i': Q2_i, 'Q2_ii': Q2_ii, 'Q3_i': Q3_i, 'Q3_ii': Q3_ii}
f = open('Lab01_201830360498_yuchensong.pkl', 'wb')
pkl.dump(answer, f)
f.close()

f = open('Lab01_201830360498_yuchensong.pkl', 'rb')
ANSWER = pkl.load(f)
f.close()
print(ANSWER)
