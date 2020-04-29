'''

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prehead = ListNode(None)
        prehead.next = head
        distance = 0
        curr = head
        while curr:
            distance += 1
            curr = curr.next
        distance -= n
        curr = prehead
        for _ in range(distance):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return prehead.next
        

