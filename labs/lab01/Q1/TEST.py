import networkx as nx
import matplotlib.pyplot as plt
import pickle as pkl
if __name__ == '__main__':
#i
    Ga = nx.Graph()
    Gb = nx.Graph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
Ga.add_nodes_from(nodes)
Gb.add_nodes_from(nodes)

#the first graph
Ga.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'G')])
Ga.add_edges_from([('B', 'E'), ('B', 'I')])
Ga.add_edges_from([('C', 'D'), ('C', 'F')])
Ga.add_edges_from([('D', 'F'), ('D', 'G')])
Ga.add_edges_from([('E', 'G'), ('E', 'H'), ('E', 'I')])
Ga.add_edges_from([('F', 'G'), ('F', 'K')])
Ga.add_edges_from([('G', 'H'), ('G', 'K'), ('G', 'L'), ('G', 'N')])
Ga.add_edges_from([('H', 'J'), ('H', 'L')])
Ga.add_edges_from([('I', 'Q'), ('I', 'V')])
Ga.add_edges_from([('K', 'N'), ('K', 'R')])
Ga.add_edges_from([('L', 'N'), ('L', 'O'), ('L', 'Q')])
Ga.add_edges_from([('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'R'), ('M', 'S')])
Ga.add_edges_from([('N', 'R')])
Ga.add_edges_from([('O', 'Q'), ('O', 'U')])
Ga.add_edges_from([('P', 'R'), ('P', 'S')])
Ga.add_edges_from([('Q', 'U')])
Ga.add_edges_from([('S', 'T'), ('S', 'U')])
Ga.add_edges_from([('T', 'U'), ('T', 'V')])
Ga.add_edges_from([('U', 'V')])

#the second graph
Gb.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'G')])
Gb.add_edges_from([('B', 'E'), ('B', 'I')])
Gb.add_edges_from([('C', 'D'), ('C', 'F')])
Gb.add_edges_from([('D', 'G')])
Gb.add_edges_from([('E', 'B'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('E', 'J'), ('E', 'L')])
Gb.add_edges_from([('F', 'D'), ('F', 'K')])
Gb.add_edges_from([('G', 'E'), ('G', 'F'), ('G', 'K'), ('G', 'N')])
Gb.add_edges_from([('H', 'Q')])
Gb.add_edges_from([('I', 'V')])
Gb.add_edges_from([('J', 'U'), ('J', 'V')])
Gb.add_edges_from([('K', 'N')])
Gb.add_edges_from([('L', 'E'), ('L', 'G'), ('L', 'N'), ('L', 'Q')])
Gb.add_edges_from([('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'R')])
Gb.add_edges_from([('N', 'M'), ('N', 'R')])
Gb.add_edges_from([('O', 'L'), ('O', 'Q')])
Gb.add_edges_from([('P', 'M'), ('P', 'S')])
Gb.add_edges_from([('Q', 'H'), ('Q', 'L')])
Gb.add_edges_from([('R', 'K'), ('R', 'P')])
Gb.add_edges_from([('S', 'M'), ('S', 'T'), ('S', 'U')])
Gb.add_edges_from([('T', 'S'), ('T', 'V')])
Gb.add_edges_from([('U', 'J'), ('U', 'O'), ('U', 'T')])

#ii
dT1 = nx.dfs_tree(Ga, 'A')
bT1 = nx.bfs_tree(Ga, 'A')
dT2 = nx.dfs_tree(Gb, 'A')
bT2 = nx.bfs_tree(Gb, 'A')

#iii
target1 = []
target2 = []
for target in nodes:
    const = nx.shortest_path_length(Ga, 'A', target)
    target1.append((target,const))
    const = nx.shortest_path_length(Gb, 'A', target)
    target2.append((target,const))


answer = {'Q1_i_a': Ga, 'Q1_i_b': Gb, 'Q1_ii_a_DFS': dT1,
          'Q1_ii_a_DFS': bT1, 'Q1_ii_a_DFS': dT2, 'Q1_ii_a_BFS': bT2,
          'Q1_iii_a': target1, 'Q1_iii_b': target2}
print(dT1.edges())
f = open ('lab01_Q1_201830360498_yuchensong', 'wb')
pkl.dump(answer, f)
f.close()