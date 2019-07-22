=begin
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
=end

# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    slow = nums[0]
    fast = nums[0]
    loop do
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast
            break
        end
    end

    p1 = nums[0]
    p2 = slow
    while p1 != p2
        p1 = nums[p1]
        p2 = nums[p2]
    end
    
    return p1
end

