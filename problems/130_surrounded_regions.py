'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        self.ROWS = len(board)
        self.COLS = len(board[0])
        
        from itertools import product
        borders = list(product(range(self.ROWS), [0, self.COLS - 1])) + list(product([0, self.ROWS - 1], range(self.COLS)))
        for row, col in borders:
            self.dfs(board, row, col)
        
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
            
    
    def dfs(self, board, row, col):
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS:
            return
        if board[row][col] == 'O':
            board[row][col] = 'E'
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                self.dfs(board, row + dr, col + dc)
                
