'''
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
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            isNeg = True
            x *= -1
        else:
            isNeg = False
            
        sol = 0
        while x > 0:
            sol = sol*10 + x%10
            x = x // 10
            
        if isNeg:
            sol *= -1
            
        if sol < -2**31 or sol > 2**31 - 1:
            return 0
        
        return sol

