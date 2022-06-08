import minimax
tree = minimax.BiTree()
list_of_leafs = [3, 5, 6, 9]
tree.build_by_list(list_=list_of_leafs, depth=2)
tree.fill(max_first=False)
tree.view_in_graph()