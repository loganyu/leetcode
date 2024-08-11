'''
You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.



Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.
'''

class Solution:
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    class ArticulationPointInfo:
        def __init__(self, has_articulation_point, time):
            self.has_articulation_point = has_articulation_point
            self.time = time

    def minDays(self, grid):
        rows, cols = len(grid), len(grid[0])
        ap_info = self.ArticulationPointInfo(False, 0)
        land_cells = 0
        island_count = 0
        discovery_time = [
            [-1] * cols for _ in range(rows)
        ]
        lowest_reachable = [
            [-1] * cols for _ in range(rows)
        ]
        parent_cell = [
            [-1] * cols for _ in range(rows)
        ]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    if discovery_time[i][j] == -1:
                        self._find_articulation_points(
                            grid,
                            i,
                            j,
                            discovery_time,
                            lowest_reachable,
                            parent_cell,
                            ap_info,
                        )
                        island_count += 1
        if island_count == 0 or island_count >= 2:
            return 0
        if land_cells == 1:
            return 1
        if ap_info.has_articulation_point:
            return 1  # An articulation point exists
        return 2  # Need to remove any two land cells

    def _find_articulation_points(
        self,
        grid,
        row,
        col,
        discovery_time,
        lowest_reachable,
        parent_cell,
        ap_info,
    ):
        rows, cols = len(grid), len(grid[0])
        discovery_time[row][col] = ap_info.time
        ap_info.time += 1
        lowest_reachable[row][col] = discovery_time[row][col]
        children = 0

        # Explore all adjacent cells
        for direction in self.DIRECTIONS:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if self._is_valid_land_cell(grid, new_row, new_col):
                if discovery_time[new_row][new_col] == -1:
                    children += 1
                    parent_cell[new_row][new_col] = (
                        row * cols + col
                    )  # Set parent
                    self._find_articulation_points(
                        grid,
                        new_row,
                        new_col,
                        discovery_time,
                        lowest_reachable,
                        parent_cell,
                        ap_info,
                    )

                    # Update lowest reachable time
                    lowest_reachable[row][col] = min(
                        lowest_reachable[row][col],
                        lowest_reachable[new_row][new_col],
                    )

                    # Check for articulation point condition
                    if (
                        lowest_reachable[new_row][new_col]
                        >= discovery_time[row][col]
                        and parent_cell[row][col] != -1
                    ):
                        ap_info.has_articulation_point = True
                elif new_row * cols + new_col != parent_cell[row][col]:
                    # Update lowest reachable time for back edge
                    lowest_reachable[row][col] = min(
                        lowest_reachable[row][col],
                        discovery_time[new_row][new_col],
                    )

        # Root of DFS tree is an articulation point if it has more than one child
        if parent_cell[row][col] == -1 and children > 1:
            ap_info.has_articulation_point = True

    # Check if the given cell is a valid land cell
    def _is_valid_land_cell(self, grid, row, col):
        rows, cols = len(grid), len(grid[0])
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1

