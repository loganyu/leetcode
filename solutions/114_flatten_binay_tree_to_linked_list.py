'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# O(n) space
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_tree(root)
        
    def flatten_tree(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        left_tail = self.flatten_tree(node.left)
        right_tail = self.flatten_tree(node.right)
        
        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None
        
        if right_tail:
            return right_tail
        else:
            return left_tail

# O(1) space
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
