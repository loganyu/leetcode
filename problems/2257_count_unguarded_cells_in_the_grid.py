'''
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.



Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.


Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
'''

class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _dfs(
        self, row: int, col: int, grid: List[List[int]], direction: str
    ) -> None:
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == self.GUARD
            or grid[row][col] == self.WALL
        ):
            return

        grid[row][col] = self.GUARDED
        if direction == "U":
            self._dfs(row - 1, col, grid, "U")
        if direction == "D":
            self._dfs(row + 1, col, grid, "D")
        if direction == "L":
            self._dfs(row, col - 1, grid, "L")
        if direction == "R":
            self._dfs(row, col + 1, grid, "R")

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[self.UNGUARDED for _ in range(n)] for _ in range(m)]

        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD

        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL

        for guard in guards:
            self._dfs(guard[0] - 1, guard[1], grid, "U")  # Up
            self._dfs(guard[0] + 1, guard[1], grid, "D")  # Down
            self._dfs(guard[0], guard[1] - 1, grid, "L")  # Left
            self._dfs(guard[0], guard[1] + 1, grid, "R")  # Right

        count = sum(row.count(self.UNGUARDED) for row in grid)
        return count

