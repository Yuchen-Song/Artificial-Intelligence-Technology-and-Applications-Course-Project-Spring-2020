import minimax
import pickle as pkl
list_of_leafs = [88, 41, 67, 47, 24, 61, 89, 71, 95, 2, 23, 71, 87, 31, 14, 10, 73, 90, 71, 42, 9, 62, 13, 22, 41, 80,
                 8, 84, 41, 64, 58, 29]
tree = minimax.BiTree()
tree.build_by_list(list_=list_of_leafs, depth=5)
tree.fill(max_first=False)
tree.view_in_graph()

f = open('Q1.pkl', 'wb')
pkl.dump(tree, f)
f.close()