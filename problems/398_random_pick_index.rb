=begin
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
=end

class Solution

=begin
    :type nums: Integer[]
=end
    def initialize(nums)
        @nums = nums
    end


=begin
    :type target: Integer
    :rtype: Integer
=end
    def pick(target)
        count = 0
        result = nil
        @nums.each_with_index do |num, index|
            if num == target
                count += 1
                if rand(0...count) == 0
                    result = index
                end
            end
        end
        
        return result
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(nums)
# param_1 = obj.pick(target)

