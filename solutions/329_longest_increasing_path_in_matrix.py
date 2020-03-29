'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, self.dfs(matrix, r, c, cache, n, m))
        
        return ans
    
    def dfs(self, matrix, r, c, cache, n, m):
        if cache[r][c]:
            return cache[r][c]
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                cache[r][c] = max(cache[r][c], self.dfs(matrix, nr, nc, cache, n, m))
        
        cache[r][c] += 1
        
        return cache[r][c]

