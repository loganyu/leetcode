=begin
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
=end
:
# @param {Integer[]} num
# @return {Integer[]}
def find_disappeared_numbers(nums)
    (0...nums.length).each do |i|
        val = nums[i].abs - 1
        if nums[val] > 0
            nums[val] = -nums[val]
        end
        puts nums.inspect
    end
    
    sol = []
    (0...nums.length).each do |i|
        if nums[i] > 0
            sol << i+1
        end
    end
    
    sol
end
