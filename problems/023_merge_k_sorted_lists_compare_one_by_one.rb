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
    lists.compact!
    prehead = prev = ListNode.new(nil)
    lists.sort_by!{|l|l.val}
    while (!lists.empty?)
        lmin = lists.shift
        prev.next = lmin
        prev = prev.next
        lmin = lmin.next
        if !lmin.nil? && !lists.empty?
            if lmin.val >= lists[-1].val
                lists.push(lmin)
            else
                lists.each_with_index do |l,i|
                    if l.val >= lmin.val
                        lists.insert(i, lmin)
                        break
                    end
                end
            end
        end
    end
    
    prehead.next
end