'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.valid(root, None, None)
    
    def valid(self, node, lower_limit, upper_limit):
        if lower_limit != None and node.val <= lower_limit:
            return False
        if upper_limit != None and node.val >= upper_limit:
            return False
        if node.left:
            left_valid = self.valid(node.left, lower_limit, node.val)
            if not left_valid:
                return False
        if node.right:
            right_valid = self.valid(node.right, node.val, upper_limit)
            if not right_valid:
                return False
        return True