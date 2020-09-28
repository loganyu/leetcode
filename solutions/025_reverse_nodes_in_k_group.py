'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) space


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        count = 0
        while curr and count != k:
            curr = curr.next
            count += 1

        if count == k:
            curr = self.reverseKGroup(curr, k)
            while count > 0:
                temp = head.next
                head.next = curr
                curr = head
                head = temp
                count -= 1
            head = curr

        return head

# O(1) space


class Solution:
    def reverseLinkedList(self, head, k):
        prev, curr = None, head
        while k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1

        return prev

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        ktail = None
        new_head = None

        while ptr:
            count = 0
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            if count == k:
                revHead = self.reverseLinkedList(head, k)

                if not new_head:
                    new_head = revHead
                if ktail:
                    ktail.next = revHead

                ktail = head
                head = ptr
        if ktail:
            ktail.next = head

        return new_head if new_head else head
