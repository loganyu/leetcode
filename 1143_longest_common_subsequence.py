'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

If there is no common subsequence, return 0.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
'''

# recursive
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1+1, p2+1)
            return max(memo_solve(p1+1, p2), memo_solve(p1, p2+1))
        
        return memo_solve(0, 0)
        
# dp O(n*m) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r][c+1], dp[r+1][c])
        
        return dp[0][0]

# dp O(n) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        prev_col = [0] * (len(text1) + 1)
        curr_col = [0] * (len(text1) + 1)
        for r in reversed(range(len(text2))):
            for c in reversed(range(len(text1))):
                if text2[r] == text1[c]:
                    curr_col[c] = 1 + prev_col[c + 1]
                else:
                    curr_col[c] = max(prev_col[c], curr_col[c+1])
            prev_col = curr_col[:]
        
        return prev_col[0]
                