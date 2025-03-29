'''
You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queries[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.



Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106
'''

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row_count, col_count = len(grid), len(grid[0])
        result = [0] * len(queries)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for queryIndex, queryValue in enumerate(queries):
            bfs_queue = deque([(0, 0)])
            visited = [[0] * col_count for _ in range(row_count)]
            visited[0][0] = 1
            points = 0

            while bfs_queue:
                queue_size = len(bfs_queue)
                for _ in range(queue_size):
                    current_row, current_col = bfs_queue.popleft()
                    if grid[current_row][current_col] >= queryValue:
                        continue
                    points += 1
                    for row_offset, col_offset in DIRECTIONS:
                        new_row = current_row + row_offset
                        new_col = current_col + col_offset
                        if (
                            0 <= new_row < row_count
                            and 0 <= new_col < col_count
                            and not visited[new_row][new_col]
                            and grid[new_row][new_col] < queryValue
                        ):
                            bfs_queue.append((new_row, new_col))
                            visited[new_row][new_col] = 1
                result[queryIndex] = points
        return result

