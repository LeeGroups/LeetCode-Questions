def generateSubTree(list1):
    if len(list1) == 0:
        return [None]
    if len(list1) == 1:
        return [TreeNode(list1[0])]
    SubTree = []        
    for i in range(len(list1)):
        leftSubTrees = generateSubTree(list1[:i])
        rightSubTrees = generateSubTree(list1[i+1:])
        for left in leftSubTrees:
            for right in rightSubTrees:
                SubTree.append(TreeNode(list1[i],left,right))
    return SubTree
                    
def generateTrees(n: int) -> List[Optional[TreeNode]]:
    return generateSubTree(range(1,n+1))