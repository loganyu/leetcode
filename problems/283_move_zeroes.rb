=begin
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
=end

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    last_non_zero_found_at = 0
    0.upto(nums.length - 1) do |i|
        if nums[i] != 0
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1
        end
    end
end