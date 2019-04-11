=begin
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
=end

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
    subsets = [[]]
    nums.each do |num|
        new_subsets = subsets.map do |subset|
            subset + [num]
        end
        subsets.concat(new_subsets)
    end
    
    subsets
end