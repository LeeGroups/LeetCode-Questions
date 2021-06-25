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

# a helper function that outputs:
# 1. the maximum value of all paths of the subtree that has the current root as the endpoint
# 2. the maximum value of all paths of the subtree that may or may not include the current root
def max_sum_helper(root): 
    if not root:
        return 0,0
    center = root.val
    if not root.left:
        left, lc = float('-inf'), float('-inf')
    else: 
        left, lc = max_sum_helper(root.left)
        center += left
    if not root.right:
        right, lr = float('-inf'), float('-inf')
    else:        
        right, lr = max_sum_helper(root.right)
        center += right
    max_val = max(right + root.val, left + root.val, root.val)
    c = max(center,lc,lr,max_val,left,right)
    return max_val, c

def maxPathSum(root):  
    return max_sum_helper(root)[1]

# sample inputs:

#Expect 6
print( maxPathSum(array_to_TreeNode([1,2,3,None,None,None,None])))

#Expect 42
print( maxPathSum(array_to_TreeNode([-10,9,20,None,None,15,7])))

#Expect 0
print( maxPathSum( array_to_TreeNode([])))

#Expect -3
print( maxPathSum( array_to_TreeNode([-3])))

#Expect 1
print( maxPathSum( array_to_TreeNode([1,-2,-3])))

#Expect 4
print( maxPathSum( array_to_TreeNode([1,-2,3])))

#Expect 3
print( maxPathSum( array_to_TreeNode([1,-2,-3,1,3,-2,None,-1])))
