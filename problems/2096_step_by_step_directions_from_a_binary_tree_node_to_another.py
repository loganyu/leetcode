'''
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.



Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent_map = {}
        start_node = self._find_start_node(root, startValue)
        self._populate_parent_map(root, parent_map)
        q = deque([start_node])
        visited_nodes = set()
        path_tracker = {}
        visited_nodes.add(start_node)

        while q:
            current_element = q.popleft()
            if current_element.val == destValue:
                return self._backtrack_path(current_element, path_tracker)
            if current_element.val in parent_map:
                parent_node = parent_map[current_element.val]
                if parent_node not in visited_nodes:
                    q.append(parent_node)
                    path_tracker[parent_node] = (current_element, "U")
                    visited_nodes.add(parent_node)
            if (
                current_element.left
                and current_element.left not in visited_nodes
            ):
                q.append(current_element.left)
                path_tracker[current_element.left] = (current_element, "L")
                visited_nodes.add(current_element.left)
            if (
                current_element.right
                and current_element.right not in visited_nodes
            ):
                q.append(current_element.right)
                path_tracker[current_element.right] = (current_element, "R")
                visited_nodes.add(current_element.right)
        return ""

    def _backtrack_path(self, node, path_tracker):
        path = []
        while node in path_tracker:
            path.append(path_tracker[node][1])
            node = path_tracker[node][0]
        path.reverse()
        return "".join(path)

    def _populate_parent_map(self, node, parent_map):
        if not node:
            return

        if node.left:
            parent_map[node.left.val] = node
            self._populate_parent_map(node.left, parent_map)

        if node.right:
            parent_map[node.right.val] = node
            self._populate_parent_map(node.right, parent_map)

    def _find_start_node(self, node, start_value):
        if not node:
            return None

        if node.val == start_value:
            return node

        left_result = self._find_start_node(node.left, start_value)

        if left_result:
            return left_result
        return self._find_start_node(node.right, start_value)
        
