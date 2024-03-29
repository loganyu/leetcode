'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

# O(n*m) time and O(m) space
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [0 for _ in range(m+1)]
        max_len = 0
        prev = 0
        for r in range(1, n+1):
            for c in range(1, m+1):
                temp = dp[c]
                if matrix[r-1][c-1] == '1':
                    dp[c] = min(prev, dp[c-1], dp[c]) + 1
                    max_len = max(max_len, dp[c])
                else:
                    dp[c] = 0
                prev = temp

        return max_len**2

# O(n*m) time and O(n*m) time
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        max_len = 0
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if matrix[r-1][c-1] == '1':
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1]) + 1
                    max_len = max(max_len, dp[r][c])

        return max_len**2
