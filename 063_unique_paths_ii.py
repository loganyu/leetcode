'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''
# O(n) space
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [0 for _ in range(m)]
        dp[0] = 1
        for r in range(n):
            for c in range(m):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c > 0:
                    dp[c] = dp[c-1] + dp[c]
        
        return dp[m-1]

# O(n^2) space
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [[None for _ in range(m)] for _ in range(n)]
        dp[0][0] = 1
        for c in range(1,m):
            dp[0][c] = int(obstacleGrid[0][c] == 0 and dp[0][c-1] == 1)
        for r in range(1,n):
            dp[r][0] = int(obstacleGrid[r][0] == 0 and dp[r-1][0] == 1)
        for r in range(1, n):
            for c in range(1, m):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
                else:
                    dp[r][c] = 0
        
        return dp[n-1][m-1]

# O(1) space by changing input
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        obstacleGrid[0][0] = 1
        for r in range(1, n):
            obstacleGrid[r][0] = int(obstacleGrid[r][0] == 0 and obstacleGrid[r-1][0] == 1)
        for c in range(1, m):
            obstacleGrid[0][c] = int(obstacleGrid[0][c] == 0 and obstacleGrid[0][c-1] == 1)
            
        
        for r in range(1, n):
            for c in range(1, m):
                if obstacleGrid[r][c] == 0:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
                else:
                    obstacleGrid[r][c] = 0 
        
        return obstacleGrid[n-1][m-1]
