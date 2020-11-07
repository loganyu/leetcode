'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        curr1, curr2 = l1, l2
        while curr1:
            curr1 = curr1.next
            n1 += 1
        while curr2:
            curr2 = curr2.next
            n2 += 1
        
        curr1, curr2 = l1, l2
        head = None
        while n1 > 0 and n2 > 0:
            val = 0
            if n1 >= n2:
                val += curr1.val
                curr1 = curr1.next
                n1 -= 1
            if n1 < n2:
                val += curr2.val
                curr2 = curr2.next
                n2 -= 1
            
            curr = ListNode(val)
            curr.next = head
            head = curr
        
        curr1, head = head, None
        carry = 0
        while curr1:
            val = (curr1.val + carry) % 10
            carry = (curr1.val + carry) // 10
            
            curr = ListNode(val)
            curr.next = head
            head = curr
            
            curr1 = curr1.next
        
        if carry:
            curr = ListNode(carry)
            curr.next = head
            head = curr
        
        return head

