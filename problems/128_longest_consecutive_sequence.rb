=begin
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
=end

# @param {Integer[]} nums
# @return {Integer}
def longest_consecutive(nums)
    longest_streak = 0
    num_set = Set.new(nums)
    
    num_set.each do |num|
        if !num_set.include?(num - 1)
            current_num = num
            current_streak = 1
            
            while num_set.include?(current_num + 1)
                current_num += 1
                current_streak += 1
            end
            
            longest_streak = [longest_streak, current_streak].max
        end
    end
    
    return longest_streak
end