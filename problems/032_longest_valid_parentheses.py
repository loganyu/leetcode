'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = r = max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, 2 * r)
            elif r >= l:
                l = r = 0
        l = r = 0
        for i in reversed(range(len(s))):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_len = max(max_len, 2 * l)
            elif l >= r:
                l = r = 0
        
        return max_len
