import networkx as nx
import pickle as pkl
import matplotlib.pyplot as plt

f = open('Q1.pkl', 'rb')
answers = pkl.load(f)
f.close()

print(answers)

Q1_i_a = answers['Q1_i_a']
nx.draw_networkx(Q1_i_a, with_labels=True)
plt.show()

Q1_ii_a_DFS = answers['Q1_ii_a_DFS']
print('Q1_ii_a_DFS: {}'.format(Q1_ii_a_DFS))

Q1_ii_a_BFS = answers['Q1_ii_a_BFS']
print('Q1_ii_a_BFS: {}'.format(Q1_ii_a_BFS))

Q1_iii_a = answers['Q1_iii_a']
print('Q1_iii_a: {}'.format(Q1_iii_a))
'''
answer = {'Q1_i_a': Ga, 'Q1_i_b': Gb, 'Q1_ii_a_DFS': dT1.edges(),
          'Q1_ii_a_BFS': bT1.edges(), 'Q1_ii_b_DFS': dT2.edges(),
          'Q1_ii_b_BFS': bT2.edges(), 'Q1_iii_a': target1, 'Q1_iii_b': target2}
'''