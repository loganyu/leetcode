'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == word[0]:
                    if self.search(r, c, board, word):
                        return True
        return False

    def search(self, r, c, board, word):
        if len(word) == 0:
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[0]:
            return False

        tmp = board[r][c]
        board[r][c] = None
        word = word[1:]

        exists = self.search(r+1, c, board, word) or self.search(r-1, c, board,
                                                                 word) or self.search(r, c+1, board, word) or self.search(r, c-1, board, word)

        board[r][c] = tmp

        return exists
