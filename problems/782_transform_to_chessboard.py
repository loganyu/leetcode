'''
You are given an n x n binary grid board. In each move, you can swap any two rows with each other, or any two columns with each other.

Return the minimum number of moves to transform the board into a chessboard board. If the task is impossible, return -1.

A chessboard board is a board where no 0's and no 1's are 4-directionally adjacent.

 

Example 1:


Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: One potential sequence of moves is shown.
The first move swaps the first and second column.
The second move swaps the second and third row.
Example 2:


Input: board = [[0,1],[1,0]]
Output: 0
Explanation: Also note that the board with 0 in the top left corner, is also a valid chessboard.
Example 3:


Input: board = [[1,0],[1,0]]
Output: -1
Explanation: No matter what sequence of moves you make, you cannot end with a valid chessboard.
 

Constraints:

n == board.length
n == board[i].length
2 <= n <= 30
board[i][j] is either 0 or 1.
'''

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if any(board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] for i in range(n) for j in range(n)):
            return -1
        if not n // 2 <= sum(board[0]) <= (n + 1) // 2:
            return -1
        if not n // 2 <= sum(board[i][0] for i in range(n)) <= (n + 1) // 2:
            return -1
        
        col = sum(board[0][i] == i % 2 for i in range(n))
        row = sum(board[i][0] == i % 2 for i in range(n))
        if n % 2:
            if col % 2:
                col = n - col
            if row % 2:
                row = n - row
        else:
            col = min(n - col, col)
            row = min(n - row, row)
        
        return (col + row) // 2
        
