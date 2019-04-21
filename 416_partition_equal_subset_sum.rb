=begin
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
=end

# @param {Integer[]} nums
# @return {Boolean}
def can_partition(nums)
    total = nums.sum
    if total % 2 != 0
        return false
    end
    target = total / 2
    sums = Set.new([0])
    nums.each do |num|
        new_sums = Set.new
        sums.each do |sum|
            new_sum = sum + num
            if new_sum == target
                return true
            elsif new_sum < target
                new_sums.add(new_sum)
            end
        end
        sums.merge(new_sums)
    end
    
    return false
end