'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
 

Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        nxt = [[0] * n for _ in range(m)]
        nxt[startRow][startColumn] = 1

        ans = 0
        for time in range(maxMove):
            cur = nxt
            nxt = [[0] * n for _ in range(m)]
            for r, row in enumerate(cur):
                for c, val in enumerate(row):
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if 0 <= nr < m and 0 <= nc < n:
                            nxt[nr][nc] += val
                            nxt[nr][nc] %= MOD
                        else:
                            ans += val
                            ans %= MOD

        return ans
        
