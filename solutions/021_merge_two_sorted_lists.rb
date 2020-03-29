=begin
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
=end

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
    prehead = prev = ListNode.new(nil)
    while (l1 != nil && l2 != nil)
       if l1.val <= l2.val
           prev.next = l1
           l1 = l1.next
       else
           prev.next = l2
           l2 = l2.next
       end
       prev = prev.next
    end
    
    if l1.nil?
        prev.next = l2
    else
        prev.next = l1
    end
    
    prehead.next
end