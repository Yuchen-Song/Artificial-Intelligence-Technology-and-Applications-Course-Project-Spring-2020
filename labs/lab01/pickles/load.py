import pickle as pkl

# Q1
f = open('Q1.pkl', 'rb')
answers = pkl.load(f)
f.close()
Q1_i_a = answers['Q1_i_a']
Q1_i_b = answers['Q1_i_b']
Q1_ii_a_DFS = answers['Q1_ii_a_DFS']
Q1_ii_a_BFS = answers['Q1_ii_a_BFS']
Q1_ii_b_DFS = answers['Q1_ii_b_DFS']
Q1_ii_b_BFS = answers['Q1_ii_b_BFS']
Q1_iii_a = answers['Q1_iii_a']
Q1_iii_b = answers['Q1_iii_b']

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

# Q4
f = open('Q4.pkl', 'rb')
answers = pkl.load(f)
f.close()
Q4 = answers['Q4']

# write the answer to final pickle file
answer = {'Q1_i_a': Q1_i_a, 'Q1_i_b': Q1_i_b, 'Q1_ii_a_DFS': Q1_ii_a_DFS,
          'Q1_ii_a_BFS': Q1_ii_a_BFS, 'Q1_ii_b_DFS': Q1_ii_b_DFS,
          'Q1_ii_b_BFS': Q1_ii_b_BFS, 'Q1_iii_a': Q1_iii_a, 'Q1_iii_b': Q1_iii_b,
          'Q2': Q2, 'Q3': Q3, 'Q4': Q4}
f = open('Lab01_201830360498_yuchensong.pkl', 'wb')
pkl.dump(answer, f)
f.close()

f = open('Lab01_201830360498_yuchensong.pkl', 'rb')
ANSWER = pkl.load(f)
f.close()
print(ANSWER)
