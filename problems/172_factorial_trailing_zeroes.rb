=begin
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
=end

# @param {Integer} n
# @return {Integer}
def trailing_zeroes(n)
    if n == 0
        return 0
    end
    
    return n / 5 + trailing_zeroes(n / 5)
end

