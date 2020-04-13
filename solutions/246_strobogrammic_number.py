'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirrors = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        l = 0
        r = len(num) - 1
        while l <= r:
            if num[l] != mirrors.get(num[r]):
                return False
            l += 1
            r -= 1
        
        return True
        
