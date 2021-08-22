import Binary_Tree

def isCompleteTree(root):        
    stack = [root]
    complete = True
    correct = True
    while stack:
        new_stack = []
        for i in range(len(stack)):
            if correct:
                if stack[i].left:
                    new_stack.append(stack[i].left)
                else:
                    correct = False
            else:
                if stack[i].left:
                    complete = False
                    stack = []
                    break 
            if correct:
                if stack[i].right:
                    new_stack.append(stack[i].right)
                else:
                    correct = False
            else:
                if stack[i].right:
                    complete = False
                    stack = []
                    break 
        stack = new_stack
    return complete

# Sample Inputs:

# Expect True
print(isCompleteTree(Binary_Tree.List_to_Tree([1,2,3,4,5,6])))

# Expect False
print(isCompleteTree(Binary_Tree.List_to_Tree([1,2,3,4,5,None,7])))

# Expect False
print(isCompleteTree(Binary_Tree.List_to_Tree([1,2,3,4,5,6,7,8,9,10,11,12,13,None,None,15])))
