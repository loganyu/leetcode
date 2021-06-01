=begin
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
=end

# @param {Integer[]} nums
# @param {Integer} lower
# @param {Integer} upper
# @return {String[]}
def find_missing_ranges(nums, lower, upper)
    sol = []
    prev = lower - 1
    nums << upper + 1
    nums.each do |num|
        if num == prev + 2
            sol << "#{num - 1}"
        elsif num > prev + 2
            sol << "#{prev + 1}->#{num - 1}"
        end
        
        prev = num
    end
    
    sol
end

