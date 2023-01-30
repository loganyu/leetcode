'''
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.max = 0
        self.dfs(root, None, 0)
        
        return self.max
    
    def dfs(self, node, parent, length):
        if not node:
            return 0
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        
        self.max = max(self.max, length)
        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)
        
