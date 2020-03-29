=begin
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
=end

# @param {Integer[]} nums
# @param {Integer} m
# @return {Integer}
def split_array(nums, m)
    lo = nums.max
    hi = nums.sum
    while lo <= hi
        mid = lo+(hi-lo)/2
        pieces = split(nums, mid)
        if pieces > m
            lo = mid + 1
        else
            hi = mid - 1
        end
    end
    
return lo
end

def split(nums, largest_sum)
    pieces = 1
    sum = 0
    nums.each do |num|
        sum += num
        if sum > largest_sum
            sum = num
            pieces += 1
        end
    end

    pieces
end

