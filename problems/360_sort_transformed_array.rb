# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer[]}
=begin
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
=end

def sort_transformed_array(nums, a, b, c)
    nums = nums.map{|num| quad(num, a, b, c)}
    sol = []
    i = 0
    j = nums.length - 1
    if a >= 0
        index = nums.length - 1
        while i <= j
            if nums[i] >= nums[j]
                sol[index] = nums[i]
                i += 1
            else
                sol[index] = nums[j]
                j -= 1
            end
            index -= 1
        end
    else
        index = 0
        while i <= j
            if nums[i] < nums[j]
                sol[index] = nums[i]
                i += 1
            else
                sol[index] = nums[j]
                j -= 1
            end
            index += 1
        end
    end
    
    return nums
end

def quad(num, a, b, c)
   a * num**2 + b * num + c 
end