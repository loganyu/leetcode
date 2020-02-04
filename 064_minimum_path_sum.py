'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if r == m - 1 and c != n - 1:
                    grid[r][c] += grid[r][c+1]
                elif c == n - 1 and r != m - 1:
                    grid[r][c] += grid[r+1][c]
                elif r != m - 1 and c != n - 1:
                    grid[r][c] += min(grid[r][c+1], grid[r+1][c]) 
        
        return grid[0][0]

