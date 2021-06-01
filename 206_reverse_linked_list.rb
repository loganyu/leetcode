=begin
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


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
# @return {ListNode}
# recursive
def reverse_list(head)
    if head.nil? || head.next.nil?
        return head
    end
    p = reverse_list(head)
    head.next.next = head
    head.next = nil
    
    return p
end

# @param {ListNode} head
# @return {ListNode}
# iterative
def reverse_list(head)
    prev = nil
    curr = head
    while(curr != nil)
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    end
    
    return prev
end