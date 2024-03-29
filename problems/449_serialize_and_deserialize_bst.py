'''
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return self.rserialize(root, "")
    
    def rserialize(self, node, string):
        if not node:
            return string
        string += f"{node.val},"
        string = self.rserialize(node.left, string)
        string = self.rserialize(node.right, string)
        
        return string
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        nodes = deque(data.split(","))
        return self.rdeserialize(nodes, float("-inf"), float("inf"))
    
    def rdeserialize(self, nodes, lower, upper):
        if not nodes[0]:
            return
        val = int(nodes[0])
        if val < lower or val > upper:
            return
        nodes.popleft()
        root = TreeNode(val)
        root.left = self.rdeserialize(nodes, lower, val)
        root.right = self.rdeserialize(nodes, val, upper)
        
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
