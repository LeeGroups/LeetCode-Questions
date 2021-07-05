Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diam_helper(root):
    if not root:
        return [0,0]
    else:
        left, right = diam_helper(root.left), diam_helper(root.right)
        if root.left:
            left[0] += 1
        if root.right:
            right[0] += 1
        return [max(left[0],right[0]), max(left[0], right[0], left[1], right[1], left[0] + right[0])]

def diameterOfBinaryTree(root: TreeNode) -> int:
    return diam_helper(root)[1]




# sample inputs:
