import pickle as pkl

import networkx as nx

nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
edges = [('A', 'B', 120), ('A', 'C', 22), ('A', 'D', 43), ('A', 'G', 160), ('B', 'A', 120), ('B', 'E', 32),
         ('B', 'P', 17), ('C', 'A', 22), ('C', 'D', 10), ('D', 'A', 43), ('D', 'F', 17), ('E', 'B', 32),
         ('E', 'G', 62), ('E', 'H', 32), ('F', 'D', 17), ('F', 'G', 32), ('G', 'A', 160), ('G', 'K', 22),
         ('G', 'L', 23), ('G', 'N', 140), ('H', 'I', 15), ('H', 'J', 2), ('I', 'H', 15), ('I', 'Q', 60),
         ('I', 'S', 24), ('J', 'H', 2), ('K', 'T', 95), ('L', 'G', 23), ('L', 'M', 5), ('L', 'N', 12),
         ('M', 'L', 5), ('M', 'O', 25), ('M', 'Q', 96), ('M', 'R', 34), ('N', 'G', 140), ('N', 'O', 43),
         ('N', 'T', 33), ('O', 'M', 25), ('P', 'B', 17), ('P', 'E', 45), ('P', 'I', 75), ('Q', 'I', 60),
         ('Q', 'M', 96), ('R', 'M', 34), ('S', 'I', 24), ('T', 'N', 33)]
DG = nx.DiGraph()
DG.add_nodes_from(nodes)
DG.add_weighted_edges_from(edges)

cost = []
for source in nodes:
    for target in nodes:
        if source != target:
            length, path = nx.bidirectional_dijkstra(DG, source, target)
            cost.append((source, target, length))

answer = {'Q4': cost}
f = open('Q4.pkl', 'wb')
pkl.dump(answer, f)
f.close()
