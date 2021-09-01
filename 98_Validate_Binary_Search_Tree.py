def isValidBST(root):
    def testBST(root,left = float(-inf),right = float(inf)):
        if not root:
            return True
        if left < root.val and root.val < right:
            return testBST(root.left, left, min(right,root.val)) and testBST(root.right, max(left,root.val), right)
        else:
            return False
    return testBST(root)

# Sample Inputs: