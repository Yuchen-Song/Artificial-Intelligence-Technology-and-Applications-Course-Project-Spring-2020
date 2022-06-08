import networkx as nx
import matplotlib.pyplot as plt
import pickle as pkl
#i
Ga = nx.Graph()
Gb = nx.Graph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
Ga_edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'G'), ('B', 'E'), ('B', 'I'), ('C', 'D'), ('C', 'F'),
            ('D', 'F'), ('D', 'G'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('F', 'G'), ('F', 'K'), ('G', 'H'), ('G', 'K'),
            ('G', 'L'), ('G', 'N'), ('H', 'J'), ('H', 'L'), ('I', 'Q'), ('I', 'V'), ('K', 'N'), ('K', 'R'), ('L', 'N'),
            ('L', 'O'), ('L', 'Q'), ('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'R'), ('M', 'S'), ('N', 'R'), ('O', 'Q'),
            ('O', 'U'), ('P', 'R'), ('P', 'S'), ('Q', 'U'), ('S', 'T'), ('S', 'U'), ('T', 'U'), ('T', 'V'), ('U', 'V')]
Gb_edges = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'G'), ('B', 'E'), ('B', 'I'), ('C', 'D'), ('C', 'F'),
            ('D', 'G'), ('E', 'B'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('E', 'J'), ('E', 'L'), ('F', 'D'), ('F', 'K'),
            ('G', 'E'), ('G', 'F'), ('G', 'K'), ('G', 'N'), ('H', 'Q'), ('I', 'V'), ('J', 'U'), ('J', 'V'), ('K', 'N'),
            ('L', 'E'), ('L', 'G'), ('L', 'N'), ('L', 'Q'), ('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'R'), ('N', 'M'),
            ('N', 'R'), ('O', 'L'), ('O', 'Q'), ('P', 'M'), ('P', 'S'), ('Q', 'H'), ('Q', 'L'), ('R', 'K'), ('R', 'P'),
            ('S', 'M'), ('S', 'T'), ('S', 'U'), ('T', 'S'), ('T', 'V'), ('U', 'J'), ('U', 'O'), ('U', 'T')]
Ga.add_nodes_from(nodes)
Gb.add_nodes_from(nodes)
Ga.add_edges_from(Ga_edges)
Gb.add_edges_from(Gb_edges)

#ii
dT1 = nx.dfs_tree(Ga, 'A')
bT1 = nx.bfs_tree(Ga, 'A')
dT2 = nx.dfs_tree(Gb, 'A')
bT2 = nx.bfs_tree(Gb, 'A')

#iii
target1 = []
target2 = []
for target in nodes:
    length1 = nx.shortest_path_length(Ga, 'A', target)
    target1.append((target,length1))
    length2 = nx.shortest_path_length(Gb, 'A', target)
    target2.append((target,length2))


answer = {'Q1_i_a': Ga, 'Q1_i_b': Gb, 'Q1_ii_a_DFS': dT1.edges(),
          'Q1_ii_a_BFS': bT1.edges(), 'Q1_ii_b_DFS': dT2.edges(),
          'Q1_ii_b_BFS': bT2.edges(), 'Q1_iii_a': target1, 'Q1_iii_b': target2}

f = open('Q1.pkl', 'wb')
pkl.dump(answer, f)
f.close()