class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# a function that converts a list into a tree 
def List_to_Tree(list1):
    if not list1:
        return None
    left = []
    right = []
    level = 1
    list2 = list1[1:]
    while list2:
        index = 2 ** (level - 1)
        left.extend(list2[:index])
        right.extend(list2[index : 2*index])
        list2 = list2[2*index:]
        level += 1
    if not left:
        left_Node = None
    else:
        left_Node = List_to_Tree(left)    
    if not right:
        right_Node = None
    else:
        right_Node = List_to_Tree(right)
    return TreeNode(list1[0],left_Node,right_Node)



# a function that prints out a tree
def Tree_print(root):
    stack = [root]
    while stack:
        new_stack = []
        layor = []
        for i in range(len(stack)):
            if stack[i]:
                layor.append(stack[i].val)
                new_stack.extend([stack[i].left,stack[i].right])
            else:
                layor.append("None")
        print(layor)
        stack = new_stack

# Sample Input
Tree_print(List_to_Tree([1,2,3,4,5,6]))

Tree_print(List_to_Tree([1,2,3,4,5,None,7]))
