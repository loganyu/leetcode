=begin
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
=end

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search(nums, target)
    l = 0
    r = nums.length - 1
    while l <= r
        m = r - (r-l)/2
        if nums[m] == target
            return m
        end
        if nums[l] <= nums[m]
            if target.between?(nums[l], nums[m])
                r = m - 1
            else
                l = m + 1
            end
        else
            if target.between?(nums[m], nums[r])
                l = m + 1
            else
                r = m - 1
            end
        end
    end
    
    return -1
end
