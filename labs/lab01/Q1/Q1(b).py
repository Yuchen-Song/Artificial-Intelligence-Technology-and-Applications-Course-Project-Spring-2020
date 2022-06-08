import matplotlib.pyplot as plt
import networkx as nx

if __name__ == '__main__':
    G = nx.DiGraph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
G.add_nodes_from(nodes)

G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'G')])
G.add_edges_from([('B', 'E'), ('B', 'I')])
G.add_edges_from([('C', 'D'), ('C', 'F')])
G.add_edges_from([('D', 'G')])
G.add_edges_from([('E', 'B'), ('E', 'G'), ('E', 'H'), ('E', 'I'), ('E', 'J'), ('E', 'L')])
G.add_edges_from([('F', 'D'), ('F', 'K')])
G.add_edges_from([('G', 'E'), ('G', 'F'), ('G', 'K'), ('G', 'N')])
G.add_edges_from([('H', 'Q')])
G.add_edges_from([('I', 'V')])
G.add_edges_from([('J', 'U'), ('J', 'V')])
G.add_edges_from([('K', 'N')])
G.add_edges_from([('L', 'E'), ('L', 'G'), ('L', 'N'), ('L', 'Q')])
G.add_edges_from([('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'R')])
G.add_edges_from([('N', 'M'), ('N', 'R')])
G.add_edges_from([('O', 'L'), ('O', 'Q')])
G.add_edges_from([('P', 'M'), ('P', 'S')])
G.add_edges_from([('Q', 'H'), ('Q', 'L')])
G.add_edges_from([('R', 'K'), ('R', 'P')])
G.add_edges_from([('S', 'M'), ('S', 'T'), ('S', 'U')])
G.add_edges_from([('T', 'S'), ('T', 'V')])
G.add_edges_from([('U', 'J'), ('U', 'O'), ('U', 'T')])

nx.draw_spectral(G, with_labels=True)

plt.show()
