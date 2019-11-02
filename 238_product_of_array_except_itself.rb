=begin
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
=end

# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    n = nums.length
    sol = Array.new(n, 1)
    left = 1
    1.upto(n-1).each do |i|
        left *= nums[i-1]
        sol[i] *= left
    end
    right = 1
    (n-2).downto(0).each do |j|
        right *= nums[j+1]
        sol[j] *= right
    end
    
    return sol
end
