=begin
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
=end

# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
    n = nums.length
    output = []
    backtrack(output, nums, n, 0)
    
    return output
end

def backtrack(output, nums, n, first)
    if first == n
        output.push(nums.dup)
    end
    first.upto(n-1).each do |i|
        nums[first], nums[i] = nums[i], nums[first]
        backtrack(output, nums, n, first + 1)
        nums[first], nums[i] = nums[i], nums[first]
    end
end

puts permute([1,2,3]).inspect