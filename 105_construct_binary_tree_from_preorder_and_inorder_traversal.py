'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            nonlocal pre_idx
            
            if in_left == in_right:
                return
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            index = idx_map[root.val]
            root.left = helper(in_left, index)
            root.right = helper(index + 1, in_right)
            
            return10 root
            
        
        pre_idx = 0
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder))
        
