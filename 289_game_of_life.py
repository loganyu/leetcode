'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        
        for r in range(0, n):
            for c in range(0, m):
                liveNeighbors = self.getLiveNeighbors(r, c, n, m, board)
                if board[r][c] == 1 and liveNeighbors not in [2,3]:
                    board[r][c] = "died"
                elif board[r][c] == 0 and liveNeighbors == 3:
                    board[r][c] = "born"
                    
        for r in range(0, n):
            for c in range(0, m):
                if board[r][c] == "died":
                    board[r][c] = 0
                elif board[r][c] == "born":
                    board[r][c] = 1
    
    def getLiveNeighbors(self, r, c, n, m, board):
        deltas = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        numLiveNeighbors = 0
        for dr, dc in deltas:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] in [1, "died"]:
                numLiveNeighbors += 1
        
        return numLiveNeighbors

