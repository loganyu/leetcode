'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")
        
        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend//divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)
        fraction.append(".")
        index_by_num = {}
        while remainder != 0:
            if remainder in index_by_num:
                fraction.insert(index_by_num[remainder], "(")
                fraction.append(")")
                break
            index_by_num[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder//divisor))
            remainder %= divisor
            
        return "".join(fraction)
