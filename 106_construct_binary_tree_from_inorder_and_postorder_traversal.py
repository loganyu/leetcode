'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            nonlocal post_idx
            
            if in_left > in_right:
                return None
            root = TreeNode(postorder[post_idx])
            post_idx -= 1
            index = idx_map[root.val]
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
        
        post_idx = len(postorder) - 1
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        
        return helper(0, len(inorder) - 1)

