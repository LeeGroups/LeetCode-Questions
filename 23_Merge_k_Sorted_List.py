class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_node(list1):
    if len(list1) == 0:
        return None
    elif len(list1) == 1:
        return ListNode(list1[0],None)
    else:
        return ListNode(list1[0],list_to_node(list1[1:]))

def node_to_list(node):
    list1 = []
    while node:
        list1.append(node.val)
        node = node.next
    return list1

""" def mergeKLists(lists):
    for i in range(len(lists)-1,-1,-1):
        if lists[i] == None:
            lists.pop(i)
    if lists == []:
        return None
    smallest = lists[0].val
    index = 0
    for i in range(1,len(lists)):
        if lists[i].val < smallest:
            smallest = lists[i].val
            index = i
    if lists[index].next == None:
        lists.pop(index)
    else: 
        lists[index] = lists[index].next
    return ListNode(smallest,mergeKLists(lists)) """

import heapq
def mergeKLists(lists):
    remain = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(remain,(lists[i].val,i))
    output = ListNode(-1)
    head = output
    while remain:
        value, index = heapq.heappop(remain)
        head.next = ListNode(value)
        head = head.next
        lists[index] = lists[index].next
        if lists[index]:
            heapq.heappush(remain,(lists[index].val,index))
    return output.next


# sample inputs:

#Expect [1,1,2,3,4,4,5,6]
u = [[1,4,5],[1,3,4],[2,6]]
print(node_to_list(mergeKLists([list_to_node(u[i]) for i in range(len(u))])))

#Expect ListNode()
v = [[]]
print(node_to_list(mergeKLists([list_to_node(v[i]) for i in range(len(v))])))

#Expect ListNode()
s = []
print(node_to_list(mergeKLists([list_to_node(s[i]) for i in range(len(s))])))
