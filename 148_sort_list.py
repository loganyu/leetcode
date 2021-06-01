'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Top Down Merge Sort. O(nlogn) time and O(logn) space
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def get_mid(self, head):
        mid_prev = None
        while head and head.next:
            mid_prev = head if mid_prev == None else mid_prev.next
            head = head.next.next
        mid = mid_prev.next
        mid_prev.next = None
        
        return mid
    
    def merge(self, list1, list2):
        dummy_head = ListNode()
        tail = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        tail.next = list1 if list1 else list2
        
        return dummy_head.next
        
