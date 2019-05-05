=begin
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
=end

# @param {Integer} x
# @return {Integer}
def reverse(x)
    int_max = 2**31 - 1
    int_min = -2**31
    rev = 0
    if x < 0
        neg = true
        x *= -1
    else
        neg = false
    end
    while x != 0
        pop = x % 10
        x /= 10
            
        rev = rev * 10 + pop
    end
    if rev < int_min || int_max < rev
        return 0
    end
    if neg
        rev *= -1
    end
    
    return rev
end