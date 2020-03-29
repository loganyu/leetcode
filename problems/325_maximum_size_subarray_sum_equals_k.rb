=begin
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
=end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_sub_array_len(nums, k)
    map = {}
    sum = 0
    max = 0
    nums.each_with_index do |num, i|
        sum += num
        map[sum] ||= i
        if sum - k == 0
            max = i + 1
        elsif map[sum-k] && (i - map[sum-k] > max)
            max = i - map[sum-k]
        end
    end
    
    max
end