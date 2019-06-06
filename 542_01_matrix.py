'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

from collections import deque

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        height = len(matrix)
        width = len(matrix[0])
        dist = [[float("inf") for _ in range(width)] for _ in range(height)]
        queue = deque()
        for r in range(height):
            for c in range(width):
                if matrix[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while len(queue) > 0:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < height and 0 <= nc < width:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr,nc))
        
        return dist

