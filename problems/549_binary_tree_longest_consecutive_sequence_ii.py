'''
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
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
        self.longest_path(root)
        
        return self.max
    
    def longest_path(self, node):
        if not node:
            return (0, 0)
        inr = dcr = 1
        if node.left:
            l = self.longest_path(node.left)
            if node.val == node.left.val + 1:
                dcr = l[1] + 1
            elif node.val == node.left.val - 1:
                inr = l[0] + 1
        if node.right:
            r = self.longest_path(node.right)
            if node.val == node.right.val + 1:
                dcr = max(dcr, r[1] + 1)
            elif node.val == node.right.val - 1:
                inr = max(inr, r[0] + 1)
                
        self.max = max(self.max, dcr + inr - 1)
        
        return (inr, dcr)
        
