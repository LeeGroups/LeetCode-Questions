class TreeNode:
    def __init__(self, x=0, left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    def helper(tree, a, b):
        if tree.val == a or tree.val == b:
            return [tree]
        else:                
            left = helper(tree.left,a,b) if tree.left else []
            right = helper(tree.right,a,b) if tree.right else []
            if left and right:
                return [tree]
            else:
                return left + right
    return helper(root,p,q)[0]

## beats 94.4%


# sample inputs:

#Expect 3
print(lowestCommonAncestor(TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8))),5,1).val)

#Expect 5
print(lowestCommonAncestor(TreeNode(3,TreeNode(5,TreeNode(6),TreeNode(2,TreeNode(7),TreeNode(4))),TreeNode(1,TreeNode(0),TreeNode(8))),5,4).val)

#Expect 1
print(lowestCommonAncestor(TreeNode(1,TreeNode(2),None),1,2).val)