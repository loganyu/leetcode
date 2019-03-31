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
    if nums.length == 0
        return -1
    end
    if nums.length == 1
        if nums[0] == target
            return 0
        else
            return -1
        end
    end
    rotate_index = find_rotate_index(nums)
    if nums[rotate_index] == target
        return rotate_index
    end
    if rotate_index == 0
        return binary_search(0, nums.length - 1, target, nums)
    elsif target < nums[0]
        return binary_search(rotate_index, nums.length - 1, target, nums)
    else
        return binary_search(0, rotate_index, target, nums)
    end
end

def find_rotate_index(nums)
    l = 0
    r = nums.length - 1
    if nums[l] < nums[r]
        return 0
    end
    while (l <= r)
        p = (l + r)/2
        if nums[p] > nums[p+1]
            return p + 1
        else
            if nums[p] < nums[l]
                r = p - 1
            else
                l = p + 1
            end
        end
    end
end

def binary_search(l, r, t, nums)
    while (l <= r)
        p = (l+r)/2
        if nums[p] == t
            return p
        elsif t < nums[p]
            r = p - 1
        else
            l = p + 1
        end
    end
    
    return -1        
end