def removeNthFromEnd(head, n):
    output = ListNode(0,head)
    beginning, end = output, output
    for i in range(n):
        if not end:
            return output.next
        end = end.next
    while end.next:
        beginning = beginning.next
        end = end.next
    beginning.next = beginning.next.next
    return output.next
            

# Sample Inputs: