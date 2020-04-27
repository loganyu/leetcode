'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)
        
        if rows == 0:
            return cols
        if cols == 0:
            return rows
        
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        for r in range(rows + 1):
            dp[r][0] = r
        for c in range(cols + 1):
            dp[0][c] = c
        
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
        
        return dp[rows][cols]
        
