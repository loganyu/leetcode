'''
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    total += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        
        return total
            
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.total = 0
        self.dfs(root, L, R)
        
        return self.total
    
    def dfs(self, node, L, R):
        if not node:
            return
        if L <= node.val <= R:
            self.total += node.val
        if L < node.val:
            self.dfs(node.left, L, R)
        if node.val < R:
            self.dfs(node.right, L, R) 
