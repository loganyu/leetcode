'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.



Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
'''

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0]) if num_rows > 0 else 0
        communicable_servers_count = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    can_communicate = False
                    for other_col in range(num_cols):
                        if other_col != col and grid[row][other_col] == 1:
                            can_communicate = True
                            break
                    if can_communicate:
                        communicable_servers_count += 1
                    else:
                        for other_row in range(num_rows):
                            if other_row != row and grid[other_row][col] == 1:
                                can_communicate = True
                                break
                        if can_communicate:
                            communicable_servers_count += 1

        return communicable_servers_count

