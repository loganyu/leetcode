=begin
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
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
# @return {Boolean}
def is_palindrome(head)
    if head.nil?
        return true
    end
    second_half = find_second_half(head)
    second_half = reverse_list(second_half)
    lists_equal?(head, second_half)
end

def find_second_half(head)
    slow = fast = head
    while !fast.nil? && !fast.next.nil?
        fast = fast.next.next
        slow = slow.next
    end
    if !fast.nil?
        slow = slow.next
    end
    
    return slow
end

def reverse_list(second_half)
    prev = nil
    curr = second_half
    while !curr.nil?
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    end
    
    return prev
end

def lists_equal?(head, second_half)
    while !second_half.nil?
        if head.val != second_half.val
            return false
        end
        head = head.next
        second_half = second_half.next
    end
    
    return true
end