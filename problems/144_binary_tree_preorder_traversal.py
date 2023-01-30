'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node):
            if not node:
                return
            preorder.append(node.val)
            helper(node.left)
            helper(node.right)
            
        preorder = []
        helper(root)
        
        return preorder
        
# iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return output

