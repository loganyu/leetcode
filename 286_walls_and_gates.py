'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = collections.deque()
        rows = len(rooms)
        if rows == 0:
            return
        cols = len(rooms[0])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = distance
                        queue.append((nr, nc))
            
                
        
