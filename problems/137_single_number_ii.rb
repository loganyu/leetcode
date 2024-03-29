=begin
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
=end

# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    map = {}
    nums.each do |num|
        if map[num]
            map[num] += 1
            if map[num] == 3
                map.delete(num)
            end
        else
            map[num] = 1
        end
    end
    
    map.keys[0]
end

# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)
    ones = twos = 0
    nums.each do |num|
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    end
    
    ones
end

