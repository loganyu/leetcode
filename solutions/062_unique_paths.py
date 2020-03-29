'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''
# O(n) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(m)]
        for _ in range(1, n):
            for i in range(1, m):
                dp[i] = dp[i-1] + dp[i]
        
        return dp[m-1]

# O(n^2) space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(m)] for _ in range(n)]
        for c in range(m):
            dp[0][c] = 1
        for r in range(n):
            dp[r][0] = 1
        for r in range(1, n):
            for c in range(1, m):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[n-1][m-1]

