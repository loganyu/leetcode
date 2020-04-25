'''
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        sol = []
        queue = deque([root])
        while queue:
            largest = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                largest = max(largest, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sol.append(largest)
        
        return sol

