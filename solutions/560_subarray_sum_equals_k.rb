=begin
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
=end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
    k_count = 0
    sum = 0
    count_by_sum = {}
    count_by_sum[0] = 1
    nums.each do |num|
        sum += num
        if count_by_sum[sum - k]
            k_count += count_by_sum[sum - k]
        end
        count_by_sum[sum] ||= 0
        count_by_sum[sum] += 1
    end
    
    return k_count
end