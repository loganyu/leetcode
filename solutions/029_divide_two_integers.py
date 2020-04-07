'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

# O(log^2 n) time
# O(1) space
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = MIN_INT / 2
        
        # special case: overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        quotient = 0
        while divisor >= dividend:
            power_of_two = -1
            value = divisor
            
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                power_of_two += power_of_two
            
            quotient += power_of_two
            dividend -= value
        
        return -quotient if negatives != 1 else quotient

# O(log n) time
# O(log n) space
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = MIN_INT / 2
        
        # special case: overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        doubles = []
        powers_of_two = []
        
        power_of_two = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powers_of_two.append(power_of_two)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor
            power_of_two += power_of_two
        
        quotient = 0
        
        for i in reversed(range(len(doubles))):
            if doubles[i] >= dividend:
                quotient += powers_of_two[i]
                dividend -= doubles[i]
            
        return quotient if negatives != 1 else -quotient

# O(log n) time
# O(1) space
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = MIN_INT / 2
        
        # special case: overflow
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        highest_double = divisor
        highest_power_of_two = -1
        while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
            highest_power_of_two += highest_power_of_two
            highest_double += highest_double
        
        quotient = 0
        while divisor >= dividend:
            if dividend <= highest_double:
                quotient += highest_power_of_two
                dividend -= highest_double
            
            highest_power_of_two >>= 1
            highest_double >>= 1
            
        return quotient if negatives == 1 else -quotient


