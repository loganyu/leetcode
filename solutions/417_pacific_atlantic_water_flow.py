'''
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        
        num_rows, num_cols = len(matrix), len(matrix[0])
        
        pacific_queue = deque()
        atlantic_queue = deque()
        for r in range(num_rows):
            pacific_queue.append((r,0))
            atlantic_queue.append((r, num_cols - 1))
        for c in range(num_cols):
            pacific_queue.append((0,c))
            atlantic_queue.append((num_rows - 1, c))
        
        def bfs(queue):
            reachable = set()
            while queue:
                (row, col) = queue.popleft()
                reachable.add((row, col))
                for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_row, new_col = row + x, col + y
                    if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if matrix[new_row][new_col] < matrix[row][col]:
                        continue
                    queue.append((new_row, new_col))
            return reachable
        
        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        return list(pacific_reachable & atlantic_reachable)
        
