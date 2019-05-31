=begin
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
=end

# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
    max = current_max = nums[0]
    1.upto(nums.length - 1).each do |i|
        current_max = [current_max + nums[i], nums[i]].max
        max = [max, current_max].max
    end
    
    return max
end

