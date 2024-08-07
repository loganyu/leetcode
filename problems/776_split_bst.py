'''
Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where the first subtree has nodes that are all smaller or equal to the target value, while the second subtree has all nodes that are greater than the target value. It is not necessarily the case that the tree contains a node with the value target.

Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.

Return an array of the two roots of the two subtrees in order.



Example 1:


Input: root = [4,2,6,1,3,5,7], target = 2
Output: [[2,1],[4,3,6,null,null,5,7]]
Example 2:

Input: root = [1], target = 1
Output: [[1],[]]


Constraints:

The number of nodes in the tree is in the range [1, 50].
0 <= Node.val, target <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        dummy_sm = TreeNode(0)
        cur_sm = dummy_sm
        dummy_lg = TreeNode(0)
        cur_lg = dummy_lg

        current = root
        next_node = None

        while current is not None:
            if current.val <= target:
                cur_sm.right = current
                cur_sm = current

                next_node = current.right

                cur_sm.right = None

                current = next_node
            else:
                cur_lg.left = current
                cur_lg = current

                next_node = current.left

                cur_lg.left = None

                current = next_node

        return [dummy_sm.right, dummy_lg.left]

