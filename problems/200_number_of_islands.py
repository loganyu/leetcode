'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
# bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        num_islands = 0
        nr = len(grid)
        nc = len(grid[0])
        
        for r in range(0, nr):
            for c in range(0, nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.flood_island(grid, r, c, nr, nc)
        
        return num_islands
    
    def flood_island(self, grid, r, c, nr, nc):
        stack = [(r,c)]
        while stack:
            row, col = stack.pop()
            grid[row][col] = '0'
            if row - 1 >= 0 and grid[row - 1][col] == '1':
                stack.append((row - 1, col))
            if row + 1 < nr and grid[row + 1][col] == '1':
                stack.append((row + 1, col))
            if col - 1 >= 0 and grid[row][col - 1] == '1':
                stack.append((row, col - 1))
            if col + 1 < nc and grid[row][col + 1] == '1':
                stack.append((row, col + 1))
                        
# dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    islands += 1
                    self.dfs(grid, r, c)
        
        return islands
    
    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) - 1 or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.dfs(grid, r+1, c)
        self.dfs(grid, r-1, c)
        self.dfs(grid, r, c+1)
        self.dfs(grid, r, c-1)
        
