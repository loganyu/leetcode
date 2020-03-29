=begin
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
=end

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def search_range(nums, target)
    left_idx = extreme_insertion_index(nums, target, true)
    
    if left_idx == nums.length || nums[left_idx] != target
        return [-1, -1]
    end
    
    return [left_idx, extreme_insertion_index(nums, target, false) - 1]
end

def extreme_insertion_index(nums, target, is_left)
    lo = 0
    hi = nums.length
    
    while lo < hi
        mid = lo + (hi - lo) / 2
        if nums[mid] > target || (is_left && target == nums[mid])
            hi = mid
        else
            lo = mid + 1
        end
    end
    
    return lo
end

