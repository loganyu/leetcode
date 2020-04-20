'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower, upper):
            nonlocal idx
            
            if idx == n:
                return None
            val = preorder[idx]
            if val < lower or val > upper:
                return None
            
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            
            return root
            
        idx = 0
        n = len(preorder)
        
        return helper(float('-inf'), float('inf'))

# bfs
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        
        n = len(preorder)
        root = TreeNode(preorder[0])
        stack = [root]
        
        for i in range(1, n):
            node = stack[-1]
            child = TreeNode(preorder[i])
            
            while stack and stack[-1].val < child.val:
                node = stack.pop()
                
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            
            stack.append(child)
        
        return root
