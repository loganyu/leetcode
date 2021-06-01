=begin
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
=end

# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
    last_pos = nums.length - 1
    (nums.length - 1).downto(0).each do |i|
        if i + nums[i] >= last_pos
            last_pos = i
        end
    end
    
    last_pos == 0
end

