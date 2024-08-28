'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        dummy_node = TreeNode(-1)
        dummy_node.left = root
        root = dummy_node
        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    predecessor.right = root
                    root = root.left
                else:
                    node = predecessor
                    self._reverse_subtree_links(root.left, predecessor)
                    while node != root.left:
                        result.append(node.val)
                        node = node.right
                    result.append(node.val)
                    self._reverse_subtree_links(predecessor, root.left)
                    predecessor.right = None
                    root = root.right
            else:
                root = root.right

        return result

    def _reverse_subtree_links(self, start_node, end_node):
        if start_node == end_node:
            return
        prev = None
        current = start_node
        next = None
        while current != end_node:
            next = current.right
            current.right = prev
            prev = current
            current = next
        current.right = prev

