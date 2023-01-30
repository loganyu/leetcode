'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(subtree, is_left):
            if not subtree:
                return 0
            if not subtree.left and not subtree.right:
                return subtree.val if is_left else 0
            return dfs(subtree.left, True) + dfs(subtree.right, False)
        
        return dfs(root, False)

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        curr = root
        while curr:
            if not curr.left:
                curr = curr.right
            else:
                prev = curr.left
                if not prev.left and not prev.right:
                    total += prev.val
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return total
        
