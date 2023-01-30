'''
Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
 

Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.
 

Constraints:

grid.length == m
grid[0].length == n
1 <= m, n <= 40
1 <= k <= m*n
grid[i][j] == 0 or 1
grid[0][0] == grid[m-1][n-1] == 0
'''

from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        if n == m == 1:
            return 0
        
        queue = deque([(0, 0, 0, 0)])
        visited = set()
        
        while queue:
            row, col, obstacle, path = queue.popleft()
            for r, c in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
                if 0 <= r < n and 0 <= c < m:
                    if grid[r][c] == 1 and obstacle < k and (r, c, obstacle + 1) not in visited:
                        visited.add((r, c, obstacle + 1))
                        queue.append((r, c, obstacle + 1, path + 1))
                    if grid[r][c] == 0 and (r, c, obstacle) not in visited:
                        if (r, c) == (n - 1, m - 1):
                            return path + 1
                        visited.add((r, c, obstacle))
                        queue.append((r, c, obstacle, path + 1))
        
        return -1
            
