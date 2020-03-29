'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.check(root)[1]
    
    def check(self, node):
        if node == None:
            return (0, True)
        l_depth, l_balanced = self.check(node.left)
        r_depth, r_balanced = self.check(node.right)
        
        depth = max(l_depth, r_depth) + 1
        balanced = l_balanced and r_balanced and abs(l_depth - r_depth) <= 1
        
        return (depth, balanced)

