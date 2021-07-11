class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    output = {}
    lowest = 0
    highest = 0
    def vert_helper(node, column):
        nonlocal lowest
        nonlocal highest
        if node:
            if column not in output:
                output[column] = [node.val]
            else:
                output[column].append(node.val)
            if column < lowest: 
                lowest = column
            if column > highest: 
                highest = column
            vert_helper(node.left,column-1)
            vert_helper(node.right,column+1)
    vert_helper(root,0)
    list1 = []
    for i in range(lowest,highest+1):
        if i in output:
            u = output[i] 
            u.sort()
            list1.append(u)
    return list1


# sample inputs:

# Expect [[9],[3,15],[20],[7]]
test1 = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(verticalTraversal(test1))

# Expect [[4],[2],[1,5,6],[3],[7]]
test2 = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(6)),TreeNode(3,TreeNode(5),TreeNode(7)))
print(verticalTraversal(test2))

# Expect [[4],[2],[1,5,6],[3],[7]]
test3 = TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
print(verticalTraversal(test3))
