=begin
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
def add_two_numbers(l1, l2)
    sum = l1.val + l2.val
    carry_over = sum / 10
    val = sum % 10
    lf = lp = ListNode.new(val)
    l1 = l1.next
    l2 = l2.next
    loop do
        sum = carry_over
        if !l1.nil?
            sum += l1.val
            l1 = l1.next
        end
        if !l2.nil?
            sum += l2.val
            l2 = l2.next
        end
        if l1.nil? && l2.nil?
            break
        end
        carry_over = sum / 10
        val = sum % 10
        lc = ListNode.new(val)
        lp.next = lc
        lp = lc
    end
    if sum > 0
        carry_over = sum / 10
        val = sum % 10
        lc = ListNode.new(val)
        lp.next = lc
        lp = lc

        if carry_over > 0
            lc = ListNode.new(carry_over)
            lp.next = lc
        end
    end
    
    return lf
end