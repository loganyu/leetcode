'''
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.



Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)

        while bfs_queue:
            size = len(bfs_queue)
            sum_val = 0
            for _ in range(size):
                popped_node = bfs_queue.popleft()
                sum_val += popped_node.val
                if popped_node.left is not None:
                    bfs_queue.append(popped_node.left)
                if popped_node.right is not None:
                    bfs_queue.append(popped_node.right)

            heapq.heappush(pq, sum_val)
            if len(pq) > k:
                heapq.heappop(pq)
        if len(pq) < k:
            return -1
        return pq[0]


