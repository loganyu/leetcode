'''
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false


Constraints:

The number of nodes in each tree is in the range [1, 5000].
-109 <= Node.val, target <= 109
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(curr_node, node_set):
            if not curr_node:
                return
            dfs(curr_node.left, node_set)
            node_set.add(curr_node.val)
            dfs(curr_node.right, node_set)

        node_set1, node_set2 = set(), set()
        dfs(root1, node_set1)
        dfs(root2, node_set2)

        for value1 in node_set1:
            if target - value1 in node_set2:
                return True
        return False

