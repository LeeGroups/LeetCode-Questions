class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):       
    k = 1
    start = head
    just_before = None
    while k < left:
        if not just_before:
            just_before = head
        else:
            just_before = start
        start = start.next
        k += 1
    dictionary = {}
    while k <= right:
        dictionary[k] = start
        start = start.next
        k += 1
    just_after = start
    k-=1
    while k > left:
        dictionary[k].next = dictionary[k-1]
        k -= 1
    dictionary[left].next = just_after
    if left == 1:
        return dictionary[right]
    else:
        just_before.next = dictionary[right]
        return head

# beats 84%
    

# Sample Inputs:
print(reverseBetween(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))),2,4))