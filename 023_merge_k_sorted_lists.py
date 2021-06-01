'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        prehead = point = ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id(l), l))
        while len(heap) > 0:
            _, _, node = heapq.heappop(heap)
            point.next = node
            point = point.next
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, id(node), node))
        return prehead.next
        
          
