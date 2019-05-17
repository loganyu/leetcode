=begin
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
=end

# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
    sol = []
    (0...nums.length).each do |i|
        val = nums[i].abs - 1
        if nums[val] < 0
            sol << (val + 1).abs
        else
            nums[val] = -nums[val]
        end
    end
    
    sol
end

