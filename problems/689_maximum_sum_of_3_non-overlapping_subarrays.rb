=begin
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
=end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sum_of_three_subarrays(nums, k)
    w = []
    sum = 0
    (0...nums.length).each do |i|
        sum += nums[i]
        if i >= k
            sum -= nums[i - k]
        end
        if i >= k - 1
            w[i - k + 1] = sum
        end
    end
    left = []
    best = 0
    (0...w.length).each do |i|
        if w[i] > w[best]
            best = i
        end
        left[i] = best
    end
    
    right = []
    best = w.length - 1
    (w.length - 1).downto(0).each do |i|
        if w[i] >= w[best]
            best = i
        end
        right[i] = best
    end
    puts w.inspect
    puts right.inspect
    puts left.inspect
    
    ans = [-1, -1, -1]
    (k...w.length - k).each do |m|
        l = left[m - k]
        r = right[m + k]
        al, am, ar = ans
       
        if al == -1 || w[l] + w[m] + w[r] > w[al] + w[am] + w[ar]
            ans = l, m, r
        end
    end
    
    return ans
end