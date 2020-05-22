'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque

class Codec:

    def serialize(self, root):
        string_builder = self.rserialize(root, [])
        
        return ",".join(string_builder)
    
    def rserialize(self, node, string_builder):
        if not node:
            string_builder.append("None")
        else:
            string_builder.append(str(node.val))
            string_builder = self.rserialize(node.left, string_builder)
            string_builder = self.rserialize(node.right, string_builder)
        
        return string_builder
            

    def deserialize(self, data):
        dataList = deque(data.split(','))
        return self.rdeserialize(dataList)
    
    def rdeserialize(self, dataList):
        if dataList[0] == 'None':
            dataList.popleft()
            return None
        root = TreeNode(dataList.popleft())
        root.left = self.rdeserialize(dataList)
        root.right = self.rdeserialize(dataList)
        
        return root 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

