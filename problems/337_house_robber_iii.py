'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(maxsize=None)
        def dfs(root):
            if not root:
                return 0
            val = 0
            if root.left:
                val += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                val += dfs(root.right.left) + dfs(root.right.right)
            val = max(root.val + val, dfs(root.left) + dfs(root.right))

            return val
    
        return dfs(root)
        
class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_sub(root):
            if not root:
                return [0, 0]
            left = rob_sub(root.left)
            right = rob_sub(root.right)
            res = [0, 0]
            res[0] = max(left) + max(right)
            res[1] = root.val + left[0] + right[0]
            
            return res
        
        res = rob_sub(root)
            
        return max(res)
