'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if s:
            first = p[0] in [s[0], "."]
        else:
            first = False
            
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(s)
        cols = len(p)
        dp = [[False for _ in range(cols + 1)] for _ in range(rows + 1)]
        dp[rows][cols] = True
        for r in reversed(range(rows+1)):
            for c in reversed(range(cols)):
                first = r < rows and p[c] in (s[r], '.')
                if c+1 < cols and p[c+1] == '*':
                    dp[r][c] = dp[r][c+2] or (first and dp[r+1][c])
                else:
                    dp[r][c] = first and dp[r+1][c+1]
        
        return dp[0][0]

