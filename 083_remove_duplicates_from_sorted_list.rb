=begin
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
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
def delete_duplicates(head)
    current = head
    loop do
        if current.nil? || current.next.nil?
            break
        end
        
        if current.next.val == current.val
            current.next = current.next.next
        else
            current = current.next
        end
    end
    
    return head
end