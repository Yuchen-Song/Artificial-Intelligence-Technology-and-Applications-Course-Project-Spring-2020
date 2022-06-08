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
Q2 = answers['Q2']

# Q3
f = open('Q3.pkl', 'rb')
answers = pkl.load(f)
f.close()
Q3 = answers['Q3']

# write the answer to final pickle file
answer = {'Q1': Q1, 'Q2': Q2, 'Q3': Q3}
f = open('Lab01_201830360498_yuchensong.pkl', 'wb')
pkl.dump(answer, f)
f.close()

f = open('Lab01_201830360498_yuchensong.pkl', 'rb')
ANSWER = pkl.load(f)
f.close()
print(ANSWER)
