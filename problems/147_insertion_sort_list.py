'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pre_head = ListNode()
        curr = head
        while curr:
            prev_node = pre_head
            next_node = prev_node.next
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next
            
            next_iter = curr.next
            curr.next = next_node
            prev_node.next = curr
            
            curr = next_iter
        
        return pre_head.next
        
