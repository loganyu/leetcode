=begin
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
=end

# O(n^2) runtime
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
    n = nums.length
    if n == 0
        return 0
    end
    dp = []
    dp[0] = 1
    max_ans = 1
    (1...n).each do |i|
        max_val = 0
        (0...i).each do |j|
            if nums[j] < nums[i]
                max_val = [max_val, dp[j]].max
            end
        end
        dp[i] = max_val + 1
        max_ans = [max_ans, dp[i]].max
    end
    
    return max_ans
end

# O(n log(n)) runtime
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
    n = nums.length
    if n == 0
        return 0
    end
    dp = []
    nums.each do |num|
        i = 0
        j = dp.length
        while i != j
            m = i + (j-i)/2
            if dp[m] < num
                i = m + 1
            else
                j = m
            end
        end
        dp[i] = num
    end
    
    return dp.length
end

