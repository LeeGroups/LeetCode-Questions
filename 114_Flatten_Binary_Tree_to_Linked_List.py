def helper(self, root):
    if not root.left:
        if not root.right:
            return (root,root)
        else:
            right, last = self.helper(root.right)
            root.right = right
            return (root,last)
    else:
        left, left_last = self.helper(root.left)
        if root.right:
            right, right_last = self.helper(root.right)
            root.left = None
            root.right = left
            left_last.right = right
            return (root,right_last)
        else:
            root.left = None
            root.right = left
            return (root,left_last)

def flatten(self, root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return root
    self.helper(root)
            