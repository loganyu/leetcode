=begin
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
=end

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def reverse_k_group(head, k)
    curr = head
    count = 0
    while (!curr.nil? && count != k)
        curr = curr.next
        count += 1
    end
    
    if count == k
        curr = reverse_k_group(curr, k)
        while count > 0
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            
            count -= 1  
        end
        head = curr
    end
    
    return head
end
