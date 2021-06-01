=begin
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
=end

# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def search(nums, target)
    l = 0
    r = nums.length - 1
    while l <= r
        m = r - (r-l)/2
        if nums[m] == target
            return true
        end
        while nums[l] == nums[m] && l < m
            l += 1
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
    
    return false
end