=begin
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
=end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_sliding_window(nums, k)
    n = nums.length
    if n * k == 0
        return []
    end
    if k == 1
        return nums
    end
    
    left = [0]*n
    left[0] = nums[0]
    right = [0]*n
    right[n-1] = nums[n-1]
    (1...n).each do |i|
        if i % k == 0
            left[i] = nums[i]
        else
            left[i] = [left[i-1], nums[i]].max
        end
        j = n - i - 1
        if (j+1) % k == 0
            right[j] = nums[j]
        else
            right[j] = [right[j+1], nums[j]].max
        end
    end
    
    output = []
    (0...n-k+1).each do |i|
        output << [left[i+k-1], right[i]].max
    end
    
    return output
end

