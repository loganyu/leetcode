'''
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.



Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
'''

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    def is_sub_island(self, x, y, grid1, grid2, visited):
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        is_sub_island = True

        pending_cells = deque()
        pending_cells.append((x, y))
        visited[x][y] = True

        while pending_cells:
            curr_x, curr_y = pending_cells.popleft()
            if not self.is_cell_land(curr_x, curr_y, grid1):
                is_sub_island = False

            for direction in self.directions:
                next_x = curr_x + direction[0]
                next_y = curr_y + direction[1]
                if (
                    0 <= next_x < total_rows
                    and 0 <= next_y < total_cols
                    and not visited[next_x][next_y]
                    and self.is_cell_land(next_x, next_y, grid2)
                ):
                    pending_cells.append((next_x, next_y))
                    visited[next_x][next_y] = True

        return is_sub_island

    def countSubIslands(
        self, grid1: List[List[int]], grid2: List[List[int]]
    ) -> int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])

        visited = [[False] * total_cols for _ in range(total_rows)]
        sub_island_counts = 0

        for x in range(total_rows):
            for y in range(total_cols):
                if (
                    not visited[x][y]
                    and self.is_cell_land(x, y, grid2)
                    and self.is_sub_island(x, y, grid1, grid2, visited)
                ):
                    sub_island_counts += 1
        return sub_island_counts
