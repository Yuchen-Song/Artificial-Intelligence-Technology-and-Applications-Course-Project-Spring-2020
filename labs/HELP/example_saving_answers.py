import networkx as nx
import pickle as pkl

nodes = [1,2,3,4]
edges = [(1,2),(1,3),(3,2),(3,4),(4,3)]

graph = nx.DiGraph()
graph.add_nodes_from(nodes)
graph.add_edges_from(edges)

source = 1

visited_edges_dfs = nx.dfs_tree(graph, source)
visited_edges_bfs = nx.bfs_tree(graph, source)

cost_from_tar = []
for target in nodes:
    cost = nx.shortest_path_length(graph, source, target)
    cost_from_tar.append((target, cost))

answers = {'Q1_i_a': graph, 'Q1_ii_a_DFS': visited_edges_dfs.edges(), 'Q1_ii_a_BFS': visited_edges_bfs.edges(), 'Q1_iii': cost_from_tar}

f = open('Lab01_Q1_20190123456789_chentao.pkl', 'wb')
pkl.dump(answers, f)
f.close()