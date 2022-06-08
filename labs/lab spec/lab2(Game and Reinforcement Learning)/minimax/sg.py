
def SG(sg, son):
    """
    :param sg: It is a list with only value 1 or 0. sg[i] == 1 means when there are i targets left, the first player wins.
    :param son: It stores the following state of the state right now.
    :param start:the beginning of sg, the state before need to be initialized
    :param n: The number of targets.
    :return: It returns sg[n], which is the answer we are looking for
    """
    for i in range(1, len(sg)):
        res = 1
        for j in son[i]:
            res = min(res, sg[j])
        sg[i] = 1 - res
