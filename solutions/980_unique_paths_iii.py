'''
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        non_obstacles = 0
        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row, start_col = row, col
        
        path_count = 0
        
        def backtrack(row, col, remain):
            nonlocal path_count
            
            if grid[row][col] == 2 and remain == 1:
                path_count += 1
                return
            
            temp = grid[row][col]
            grid[row][col] = -1
            remain -= 1
            
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                next_row, next_col = row + dr, col + dc
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                if grid[next_row][next_col] < 0:
                    continue
                backtrack(next_row, next_col, remain)
            grid[row][col] = temp
        
        backtrack(start_row, start_col, non_obstacles)
        
        return path_count
        
