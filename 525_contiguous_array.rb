'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)
    map = {0 => -1}
    max_len = 0
    count = 0
    nums.each_with_index do |num, i|
        count = count + (num == 1 ? 1 : -1)
        if map[count]
            max_len = [max_len, i - map[count]].max
        else
            map[count] = i
        end
    end
    
    return max_len
end

