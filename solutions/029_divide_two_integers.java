/*
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
*/

class Solution {
    private static int HALF_INT_MIN = -1073741824;
    
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        
        int negatives = 2;
        if (dividend > 0) {
            negatives--;
            dividend = -dividend;
        }
        if (divisor > 0) {
            negatives--;
            divisor = -divisor;
        }
        
        int highestDouble = divisor;
        int highestPowerOfTwo = -1;
        while (highestDouble >= HALF_INT_MIN && dividend <= highestDouble + highestDouble) {
            highestPowerOfTwo += highestPowerOfTwo;
            highestDouble += highestDouble;
        }
        int quotient = 0;
        while (dividend <= divisor) {
            if (dividend <= highestDouble) {
                quotient += highestPowerOfTwo;
                dividend -= highestDouble;
            }
            highestPowerOfTwo >>= 1;
            highestDouble >>= 1;
        }
        
        if (negatives != 1)
            return -quotient;
        return quotient;
    }
}

