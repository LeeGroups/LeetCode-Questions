# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "*"
        if root.left == None:
            left = "*"
        else: 
            left = self.serialize(root.left)
        if root.right == None:
            right = "*"
        else:
            right = self.serialize(root.right)
        
        return str(root.val) + "[" + left + "]" + "(" + right + ")"        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "*":
            return None
        i = 0
        while data[i] != "[": 
            i += 1
        j = i
        k = 1
        while k != 0:
            j += 1
            if data[j] == "]":
                k -= 1
            elif data[j] == "[":
                k += 1
        return TreeNode(int(data[0:i]),self.deserialize(data[i+1:j]),self.deserialize(data[j+2:len(data)-1]))


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# sample inputs:

test1 = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
ser1 = Codec().serialize(test1)
print(ser1)
deser = Codec().deserialize(ser1)
print(deser)
ser2 = Codec().serialize(deser)
print(ser2)