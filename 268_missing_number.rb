=begin
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
=end

# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
    expected_sum = nums.length*(nums.length+1)/2
    actual_sum = nums.sum
    
    expected_sum - actual_sum
end