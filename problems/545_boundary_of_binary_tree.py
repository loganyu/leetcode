'''
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        if not self.is_leaf(root):
            res.append(root.val)
        self.add_left_boundary(root.left, res)
        self.add_leaves(root, res)
        self.add_right_boundary(root.right, res)
        return res
    
    def is_leaf(self, node):
        return node.left == None and node.right == None
        
    def add_left_boundary(self, node, res):
        while node:
            if not self.is_leaf(node):
                res.append(node.val)
            node = node.left or node.right
    
    def add_leaves(self, node, res):
        if self.is_leaf(node):
            res.append(node.val)
        else:
            if node.left:
                self.add_leaves(node.left, res)
            if node.right:
                self.add_leaves(node.right, res)
    
    def add_right_boundary(self, node, res):
        right_nodes = collections.deque()
        while node:
            if not self.is_leaf(node):
                right_nodes.appendleft(node.val)
            node = node.right or node.left
        res.extend(right_nodes)
        
