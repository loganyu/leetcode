=begin
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
=end

# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
    if n < 0
        x = 1 / x
        n = -n
    end
    ans = 1
    current_product = x
    
    while n > 0
        if n % 2 == 1
            ans = ans * current_product
        end
        current_product = current_product * current_product
        n /= 2
    end
    
    return ans
end