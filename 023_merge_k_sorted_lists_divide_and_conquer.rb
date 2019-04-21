=begin
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
=end

# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode[]} lists
# @return {ListNode}
def merge_k_lists(lists)
    while lists.length > 1
        merged_list = merge_2_lists(lists.shift, lists.shift)
        lists.push(merged_list)
    end
    
    lists[0]
end
    
def merge_2_lists(l1, l2)
    prehead = curr = ListNode.new(nil)
    while l1 && l2
        if l1.val <= l2.val
            curr.next = l1
            l1 = l1.next
        else
            curr.next = l2
            l2 = l1
            l1 = curr.next.next
        end
        curr = curr.next
    end
    if l1.nil?
        curr.next = l2
    else
        curr.next = l1
    end
            
    return prehead.next
end