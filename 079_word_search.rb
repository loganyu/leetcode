=begin
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
=end

# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def exist(board, word)
    board.each_with_index do |row, i|
        row.each_with_index do |char, j|
            visited = []
            if search(word, board, i, j)
                return true
            end
        end
    end
    
    return false
end

def search(word, board, i, j)
    if word.length == 0
        return true
    end

    if out_of_bounds(board, i, j) || word[0] != board[i][j]
        return false
    end

    tmp = board[i][j]
    board[i][j] = nil
    word = word[1..-1]

    exists = search(word, board, i+1, j) ||
        search(word, board, i-1, j) ||
        search(word, board, i, j+1) ||
        search(word, board, i, j-1)
    board[i][j] = tmp
    
    return exists
end

def out_of_bounds(board, i, j)
   return i < 0 || j < 0 || i >= board.length || j >= board[0].length 
end
