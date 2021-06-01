=begin
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
=end

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def wiggle_sort(nums)
    inc = true
    (0...nums.length-1).each do |i|
        if inc
            if nums[i] > nums[i+1]
                nums[i], nums[i+1] = nums[i+1], nums[i]
            end
        else
            if nums[i] < nums[i+1]
                nums[i], nums[i+1] = nums[i+1], nums[i]
            end
        end
        inc = !inc
    end
    
    nums
end

