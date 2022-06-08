import networkx as nx
import pickle as pkl
import matplotlib.pyplot as plt

f = open('Lab01_Q1_20190123456789_chentao.pkl', 'rb')
answers = pkl.load(f)
f.close()

print(answers)

graph = answers['Q1_i_a']
nx.draw_networkx(graph, with_labels=True)
plt.show()

Q1_ii_a_DFS = answers['Q1_ii_a_DFS']
print('Q1_ii_a_DFS: {}'.format(Q1_ii_a_DFS))

Q1_ii_a_BFS = answers['Q1_ii_a_BFS']
print('Q1_ii_a_BFS: {}'.format(Q1_ii_a_BFS))

Q1_iii = answers['Q1_iii']
print('Q1_iii: {}'.format(Q1_iii))