=begin
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
=end

# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    ans = 0
    nums.each do |num|
        ans = ans ^ num
    end
    
    ans
end

