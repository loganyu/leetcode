=begin
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
=end

# @param {Integer[]} digits
# @return {Integer[]}
def plus_one(digits)
    (digits.length - 1).downto(0).each do |i|
       if digits[i] < 9
           digits[i] += 1
           return digits
       else
           digits[i] = 0
       end
    end
    
    return digits.unshift(1)
end

