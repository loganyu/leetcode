=begin
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
=end
def three_sum(nums)
    result = []
    if nums.length < 3
      return result
    end
    nums.sort!
    
    0.upto(nums.length - 3).each do |i|
      if i > 0 && nums[i] == nums[i-1]
        next
      end
      low = i+1
      high = nums.length-1
      while (low < high)
          sum = nums[low] + nums[high] + nums[i]
          if (sum == 0)
            result.push([nums[low],nums[high],nums[i]].sort)
            while (low < high && nums[low] == nums[low+1])
                low += 1
            end
            while (low < high && nums[high] == nums[high-1])
                high -= 1
            end
            low += 1
            high -= 1
          elsif sum < 0
            low += 1
          else
            high -= 1
          end
      end
    end

    result
end

nums = [-1,0,1,2,-1,-4]
puts three_sum(nums).inspect