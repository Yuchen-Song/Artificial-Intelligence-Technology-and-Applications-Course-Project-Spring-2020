import networkx as nx
import matplotlib.pyplot as plt
import pickle as pkl
if __name__ == '__main__':
    G = nx.Graph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
G.add_nodes_from(nodes)

G.add_edges_from([('A', 'B'), ('A', 'E'), ('A', 'G'), ('A', 'D'), ('A', 'C')])
G.add_edges_from([('B', 'I'), ('B', 'E')])
G.add_edges_from([('C', 'D'), ('C', 'F')])
G.add_edges_from([('D', 'F'), ('D', 'G')])
G.add_edges_from([('E', 'I'), ('E', 'H'), ('E', 'G')])
G.add_edges_from([('F', 'G'), ('F', 'K')])
G.add_edges_from([('G', 'H'), ('G', 'L'), ('G', 'K'), ('G', 'N')])
G.add_edges_from([('H', 'L'), ('H', 'J')])
G.add_edges_from([('I', 'V'), ('I', 'Q')])
G.add_edges_from([('K', 'N'), ('K', 'R')])
G.add_edges_from([('L', 'N'), ('L', 'O'), ('L', 'Q')])
G.add_edges_from([('M', 'N'), ('M', 'O'), ('M', 'R'), ('M', 'S'), ('M', 'P')])
G.add_edges_from([('N', 'R')])
G.add_edges_from([('O', 'Q'), ('O', 'U')])
G.add_edges_from([('P', 'R'), ('P', 'S')])
G.add_edges_from([('Q', 'U')])
G.add_edges_from([('S', 'T'), ('S', 'U')])
G.add_edges_from([('T', 'U'), ('T', 'V')])
G.add_edges_from([('U', 'V')])

nx.draw_spring(G, with_labels=True)

plt.show()
