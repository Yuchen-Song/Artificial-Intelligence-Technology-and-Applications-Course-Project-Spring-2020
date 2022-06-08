import networkx as nx
import matplotlib.pyplot as plt
import pickle as pkl

nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
DG = nx.DiGraph()
DG.add_nodes_from(nodes)
edges = [(1, 2, 2), (1, 3, 3), (1, 5, 1), (2, 3, 10), (3, 4, 1), (4, 8, 2), (5, 7, 2), (6, 12, 1),
         (6, 13, 2), (7, 6, 1), (7, 8, 5), (8, 9, 2), (8, 14, 3), (11, 8, 4), (14, 10, 1), (14, 11, 2)]
DG.add_weighted_edges_from(edges)

source = 1
path = []
for target in nodes:
    length = nx.dijkstra_path_length(DG, source, target)
    path.append((target, length))

answer = {'Q2': path}
f = open('Q2.pkl', 'wb')
pkl.dump(answer, f)
f.close()