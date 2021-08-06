class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(subtree):
            if not subtree:
                return [0, float('-inf'), float('inf')]
            if subtree.left:
                left_biggest_diff, left_min_val, left_max_val = helper(subtree.left)
                left_min = min(subtree.val, left_min_val) 
                left_max = max(subtree.val, left_max_val)
                left_current = max(left_biggest_diff, abs(subtree.val - left_min), abs(subtree.val - left_max))
            else: 
                left_min = subtree.val
                left_max = subtree.val
                left_current = float('-inf')
            if subtree.right:
                right_biggest_diff, right_min_val, right_max_val = helper(subtree.right)
                right_min = min(subtree.val, right_min_val)
                right_max = max(subtree.val, right_max_val)
                right_current = max(right_biggest_diff, abs(subtree.val - right_min), abs(subtree.val - right_max))            
            else: 
                right_min = subtree.val
                right_max = subtree.val
                right_current = float('-inf')
            return [max(left_current, right_current), min(left_min,right_min), max(left_max, right_max)]

        return helper(root)[0]

# faster than 85%