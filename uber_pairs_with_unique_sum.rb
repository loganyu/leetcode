# Input: [9, 4, 3, 1, 7, 12]
# Output: [1, 12] & [4, 9], [3, 7] & [1, 9], [4, 12] & [7, 9]

def pairs_with_unique_sum(nums)
  pairs_by_sum = {}
  (0...nums.length - 1).each do |i|
    (i+1...nums.length).each do |j|
      pairs_by_sum[nums[i]+nums[j]] ||= []
      pairs_by_sum[nums[i]+nums[j]] << [nums[i], nums[j]]
    end
  end

  pairs_by_sum.select{|k,v| v.length > 1}.values
end

nums = [9, 4, 3, 1, 7, 12]
puts pairs_with_unique_sum(nums).inspect