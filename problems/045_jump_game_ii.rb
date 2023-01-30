=begin
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
=end

# @param {Integer[]} nums
# @return {Integer}
def jump(nums)
    if nums.length < 2
        return 0
    end
    curr_farthest = curr_end = jumps = 0
    nums.each_with_index do |num, i|
        curr_farthest = [i + num, curr_farthest].max
        if i == curr_end
            jumps += 1
            curr_end = curr_farthest
        end
        if curr_end >= nums.length - 1
            break
        end
    end
    
    return jumps
end

