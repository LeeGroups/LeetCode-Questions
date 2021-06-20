class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):
    if root == None:
        return 0
    if low <= root.val <= high:
        return root.val + rangeSumBST(root.left,low,high) + rangeSumBST(root.right,low,high)
    elif low <= root.val:
        return rangeSumBST(root.left,low,high)
    elif root.val <= high:
        return rangeSumBST(root.right,low,high)
    else:
        return 0


# sample inputs:

# Expect 32
test1 = TreeNode(10, TreeNode(5, TreeNode(3),TreeNode(7)), TreeNode(15,None,TreeNode(18)))
print(rangeSumBST(test1,7,15))

# Expect 23
test2 = TreeNode(10, TreeNode(5,TreeNode(3,TreeNode(1),None),TreeNode(7,TreeNode(6),None)), TreeNode(15,TreeNode(13),TreeNode(18)))
print(rangeSumBST(test2,6,10))
