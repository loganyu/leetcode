=begin
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
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
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
    prehead = ListNode.new(nil)
    prehead.next = head
    first = prehead
    second = prehead
    (n+1).times do
        first = first.next
    end
    while !first.nil?
        first = first.next
        second = second.next
    end
    second.next = second.next.next
    
    return prehead.next
end

