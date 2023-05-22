'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        first_x, first_y = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    first_x, first_y = i, j
                    break

        def dfs(x, y):
            grid[x][y] = 2
            queue.append((x,y))
            for cur_x, cur_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                    dfs(cur_x, cur_y)

        queue = [(first_x, first_y)]
        dfs(first_x, first_y)

        distance = 0
        while queue:
            next_queue = []
            for x, y in queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            next_queue.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = 2
            queue = next_queue
            distance += 1

