"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ai = len(a) - 1
        bi = len(b) - 1
        carry = 0
        ans = []
        while ai >= 0 or bi >= 0 or carry > 0:
            if ai >= 0 and a[ai] == '1':
                carry += 1
            if bi >= 0 and b[bi] == '1':
                carry += 1
            
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')
            
            carry //= 2
            ai -= 1
            bi -= 1
        
        ans.reverse()
        return "".join(ans)
