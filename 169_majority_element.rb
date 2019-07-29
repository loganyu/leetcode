=begin
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
=end

# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    n = nums.length
    count_by_num = {}
    nums.each do |num|
        count_by_num[num] ||= 0
        count_by_num[num] += 1
        if count_by_num[num] > n/2
            return num
        end
    end
end

