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
        carry_over = 0
        sol = []
        while ai >= 0 or bi >= 0 or carry_over > 0:
            total = carry_over
            if ai >= 0:
                total += int(a[ai])
            if bi >= 0:
                total += int(b[bi])
            carry_over = total // 2
            sol.append(str(total % 2))
            
            ai -= 1
            bi -= 1
        
        return "".join(sol[::-1])
