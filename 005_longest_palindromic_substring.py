'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            s1, e1 = self.expandAroundCenter(s, i, i)
            s2, e2 = self.expandAroundCenter(s, i, i+1)
            if e1 - s1 > end - start:
                start, end = s1, e1
            if e2 - s2 > end - start:
                start, end = s2, e2    
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, start: int, end: int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        
        return start + 1, end - 1

