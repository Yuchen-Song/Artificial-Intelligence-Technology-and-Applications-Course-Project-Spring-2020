import minimax
sg = [0 for i in range(6)]
# when we have 4 coins,
# sg should be initialized with [0, 0, 0, 0, 0]
son = [[],[0],[0,1],[3-1,3-2],[4-1,4-2],[5-1,5-2]]
# if we can only take 1 or 2 coins one time.
# son[0] is [] as 0 coins left
minimax.SG(sg, son)
print(sg)
# sg = [0, 1, 1, 0, 1]