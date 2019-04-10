=begin
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
=end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_kth_largest(nums, k)
    loop do
        pivot = nums.delete_at(rand(nums.length))
        left, right = nums.partition{|num| num > pivot}
        if k == left.length + 1
            return pivot
        elsif k < left.length + 1
            nums = left
        else
            k = k - left.length - 1
            nums = right
        end
    end
end
