class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortedListToBST(head):
    list1 = []
    while not head:
        list1.append(head.val)
        head = head.next
    def ListToBST(List):
        if not List:
            return None
        n = len(List) // 2
        return TreeNode(List[n],ListToBST(List[:n]),ListToBST(List[n+1:]))





# Sample Inputs:
