#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def array_to_TreeNode(list1):
    n = len(list1)
    if n == 0:
        return None 
    elif list1 == [None]:
        return None
    left_list = []
    right_list = []
    depth = 0
    i = 1
    k = 1
    while i < n:
        if k <= 2** depth:
            left_list += [list1[i]]
            i += 1
            k += 1
        elif k <= 2 ** (depth +1):
            right_list += [list1[i]]
            k += 1
            i += 1
        else:
            depth += 1
            k = 1
    left = array_to_TreeNode(left_list)
    right = array_to_TreeNode(right_list)
    return TreeNode(list1[0],left,right) 

def rightSideView(root):
    if root == None:
        return []
    right_side = rightSideView(root.right) 
    left_side = rightSideView(root.left) 
    return [root.val] + right_side + left_side[len(right_side):]

# sample inputs:

#Expect [1,3,4]
print( rightSideView(array_to_TreeNode([1,2,3,None,5,None,4])))

#Expect [1,3]
print( rightSideView(array_to_TreeNode([1,None,3])))

#Expect []
print( rightSideView( array_to_TreeNode([])))


