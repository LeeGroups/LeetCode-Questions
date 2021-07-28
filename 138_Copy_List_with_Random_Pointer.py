import collections

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    temp = head
    dictionary = collections.defaultdict(Node)
    while temp != None:
        dictionary[temp] = Node(temp.val)
        temp = temp.next
    temp2 = head
    while temp2 != None:
        if temp2.next:
            dictionary[temp2].next = dictionary[temp2.next]
        if temp2.random:
            dictionary[temp2].random = dictionary[temp2.random]
        temp2 = temp2.next
    return dictionary[head]