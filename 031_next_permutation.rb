=begin
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
=end

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def next_permutation(nums)
    i = nums.length - 2
    while i >= 0 && nums[i+1] <= nums[i]
        i -= 1
    end
    if i >= 0
        j = nums.length - 1
        while (j >= i && nums[j] <= nums[i])
            j -= 1
        end
        nums[i], nums[j] = nums[j], nums[i]
    end
    
    invert_numbers(nums, i+1)
end

def invert_numbers(nums, start_index)
    i = start_index
    j = nums.length - 1
    while (i < j)
        nums[i], nums[j] =  nums[j], nums[i]
        i += 1
        j -= 1
    end
end