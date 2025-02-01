'''
You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

If isWater[i][j] == 0, cell (i, j) is a land cell.
If isWater[i][j] == 1, cell (i, j) is a water cell.
You must assign each cell a height in a way that follows these rules:

The height of each cell must be non-negative.
If the cell is a water cell, its height must be 0.
Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.



Example 1:



Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.
Example 2:



Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.


Constraints:

m == isWater.length
n == isWater[i].length
1 <= m, n <= 1000
isWater[i][j] is 0 or 1.
There is at least one water cell.


Note: This question is the same as 542: https://leetcode.com/problems/01-matrix/
'''

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        rows = len(isWater)
        columns = len(isWater[0])

        cell_heights = [[-1 for _ in range(columns)] for _ in range(rows)]

        cell_queue = deque()

        for x in range(rows):
            for y in range(columns):
                if isWater[x][y] == 1:
                    cell_queue.append((x, y))
                    cell_heights[x][y] = 0

        height_of_next_layer = 1

        while cell_queue:
            layer_size = len(cell_queue)

            for _ in range(layer_size):
                current_cell = cell_queue.popleft()

                for d in range(4):
                    neighbor_x = current_cell[0] + dx[d]
                    neighbor_y = current_cell[1] + dy[d]

                    if (
                        self._is_valid_cell(
                            neighbor_x, neighbor_y, rows, columns
                        )
                        and cell_heights[neighbor_x][neighbor_y] == -1
                    ):
                        cell_heights[neighbor_x][
                            neighbor_y
                        ] = height_of_next_layer
                        cell_queue.append((neighbor_x, neighbor_y))

            height_of_next_layer += 1

        return cell_heights

    def _is_valid_cell(self, x, y, rows, columns):
        return 0 <= x < rows and 0 <= y < columns

