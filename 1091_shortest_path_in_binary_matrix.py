'''
1091. Shortest Path in Binary Matrix
Medium

559

44

Add to List

Share
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1
'''

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1
        
        queue = deque([(0,0,1)])
        while queue:
            r, c, l = queue.popleft()
            if (r,c) == (n-1,m-1):
                return l
            for dr, dc in [(1,-1), (0,-1), (-1,-1), (0, 1), (1,1), (-1,1), (1,0), (1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, l+1))
        
        return -1
        
