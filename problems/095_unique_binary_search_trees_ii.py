'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.helper(1, n)
    
    def helper(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        for curRootVal in range(start, end+1):
            all_left_subtrees = self.helper(start, curRootVal-1)
            all_right_subtrees = self.helper(curRootVal+1, end)
            
            for left_subtree in all_left_subtrees:
                for right_subtree in all_right_subtrees:
                    curRoot = TreeNode(curRootVal)
                    curRoot.left = left_subtree
                    curRoot.right = right_subtree
                    
                    all_trees.append(curRoot)
                    
        return all_trees
    
