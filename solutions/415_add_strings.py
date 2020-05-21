'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

from collections import deque

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sol = deque()
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                total += ord(num2[j]) - ord('0')
                j -= 1
            
            sol.appendleft(str(total % 10))
            carry = total // 10
                             
        return ''.join(sol)
         
