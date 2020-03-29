=begin
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

=end

# @param {Integer} s
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(s, nums)
    ans = Float::INFINITY
    sum = 0
    l = 0
    nums.each_with_index do |num, i|
        sum += num
        while sum >= s
            ans = [ans, i + 1 - l].min
            sum -= nums[l]
            l += 1
        end
    end
    
    return ans == Float::INFINITY ? 0 : ans
end