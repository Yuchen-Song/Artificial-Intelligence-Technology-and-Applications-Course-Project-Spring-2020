import networkx as nx
import matplotlib.pyplot as plt

# write the graph
G = nx.Graph()
nodes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V']
G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'G')])
G.add_edges_from([('B', 'E'), ('B', 'I')])
G.add_edges_from([('C', 'D'), ('C', 'F')])
G.add_edges_from([('D', 'F'), ('D', 'G')])
G.add_edges_from([('E', 'G'), ('E', 'H'), ('E', 'I')])
G.add_edges_from([('F', 'G'), ('F', 'K')])
G.add_edges_from([('G', 'H'), ('G', 'K'), ('G', 'L'), ('G', 'N')])
G.add_edges_from([('H', 'J'), ('H', 'L')])
G.add_edges_from([('I', 'Q'), ('I', 'V')])
G.add_edges_from([('K', 'N'), ('K', 'R')])
G.add_edges_from([('L', 'N'), ('L', 'O'), ('L', 'Q')])
G.add_edges_from([('M', 'N'), ('M', 'O'), ('M', 'P'), ('M', 'R'), ('M', 'S')])
G.add_edges_from([('N', 'R')])
G.add_edges_from([('O', 'Q'), ('O', 'U')])
G.add_edges_from([('P', 'R'), ('P', 'S')])
G.add_edges_from([('Q', 'U')])
G.add_edges_from([('S', 'T'), ('S', 'U')])
G.add_edges_from([('T', 'U'), ('T', 'V')])
G.add_edges_from([('U', 'V')])

# nx.draw_kamada_kawai(G, with_labels=True)
# plt.show()

# write the Digraph
DG = nx.DiGraph()
DG.add_nodes_from(nodes)
DG.add_edges_from([('A', 'B'), ('A', 'E'), ('A', 'G'), ('A', 'D'), ('A', 'C')])
DG.add_edges_from([('B', 'I'), ('B', 'E')])
DG.add_edges_from([('C', 'D'), ('C', 'F')])
DG.add_edges_from([('D', 'G')])
DG.add_edges_from([('E', 'I'), ('E', 'H'), ('E', 'G'),('E', 'J')])
DG.add_edges_from([('F', 'K')])
DG.add_edges_from([('G', 'F'), ('G', 'E'), ('G', 'K'), ('G', 'N')])
DG.add_edges_from([('H', 'Q')])
DG.add_edges_from([('I', 'V')])
DG.add_edges_from([('J', 'U'), ('J', 'V')])
DG.add_edges_from([('K', 'N')])
DG.add_edges_from([('L', 'N'), ('L', 'E'), ('L', 'Q'), ('L', 'G')])
DG.add_edges_from([('M', 'N'), ('M', 'O'), ('M', 'R'), ('M', 'P')])
DG.add_edges_from([('N', 'M'), ('N', 'R')])
DG.add_edges_from([('O', 'Q'), ('O', 'L')])
DG.add_edges_from([('P', 'M'), ('P', 'S')])
DG.add_edges_from([('Q', 'H'), ('Q', 'L')])
DG.add_edges_from([('R', 'K'), ('R', 'P')])
DG.add_edges_from([('S', 'M'), ('S', 'T'), ('S', 'U')])
DG.add_edges_from([('T', 'S'), ('T', 'V')])
DG.add_edges_from([('U', 'J'), ('U', 'O'), ('U', 'T')])
# nx.draw_kamada_kawai(G, with_labels=True)
# plt.show()


# save the sequence of graph
source = 'A'
G_visited_edges_dfs = nx.dfs_tree(G, source)
G_visited_edges_bfs = nx.bfs_tree(G, source)
print(G_visited_edges_dfs.edges())
print(G_visited_edges_bfs.edges())
# save the sequence of digraph
DG_visited_edges_dfs = nx.dfs_tree(DG, source)
DG_visited_edges_bfs = nx.bfs_tree(DG, source)
print(DG_visited_edges_dfs.edges())
print(DG_visited_edges_bfs.edges())

G_cost_from_target = []
DG_cost_from_target = []
for target in nodes:
    G_cost = nx.shortest_path_length(G, source, target)
    DG_cost = nx.shortest_path_length(DG, source, target)
    G_cost_from_target.append((target, G_cost))
    DG_cost_from_target.append((target, DG_cost))

print(G_cost_from_target)
print(DG_cost_from_target)

answer = {'Q1_i_a': G,
          'Q1_i_b': DG,
          'Q1_ii_a_DFS': G_visited_edges_dfs.edges(),
          'Q1_ii_a_BFS': G_visited_edges_bfs.edges(),
          'Q1_ii_b_DFS': DG_visited_edges_dfs.edges(),
          'Q1_ii_b_BFS': DG_visited_edges_bfs.edges(),
          'Q1_iii_a': G_cost_from_target,
          'Q1_iii_b': DG_cost_from_target}

