'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''

from collections import deque

class Solution:
    def __init__(self):
        self.EMPTY = 0
        self.BUILDING = 1
        self.OBSTACLE = 2
        
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        distances = [[0 for _ in range(m)] for _ in range(n)]
        reachable_buildings = [[0 for _ in range(m)] for _ in range(n)]
        buildings = 0
        
        for r in range(n):
            for c in range(m):
                if grid[r][c] == self.BUILDING:
                    buildings += 1
                    self.bfs(r, c, grid, distances, reachable_buildings, n, m)
        
        shortest_distance = -1
        for r in range(n):
            for c in range(m):
                if reachable_buildings[r][c] == buildings:
                    if shortest_distance == -1 or shortest_distance > distances[r][c]:
                        shortest_distance = distances[r][c]
        
        return shortest_distance
                        
    
    def bfs(self, r, c, grid, distances, reachable_buildings, n, m):
        distance = 1
        queue = deque([(r, c)]) 
        visited = set([(r, c)])
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if not 0 <= row < n or not 0 <= col < m or grid[row][col] != self.EMPTY or (row, col) in visited:
                        continue
                    distances[row][col] += distance
                    reachable_buildings[row][col] += 1
                    queue.append((row, col))
                    visited.add((row, col))
            distance += 1
