=begin
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
=end

# @param {Integer[][]} board
# @return {Void} Do not return anything, modify board in-place instead.

#store two bits for each space
# [2nd bit, 1st bit] = [next state, current state]
def game_of_life(board)
    (0...board.length).each do |r|
        (0...board[0].length).each do |c|
            live_neighbors = get_live_neighbors(board, r, c)
            if board[r][c] == 1 && [2,3].include?(live_neighbors)
                board[r][c] = 3 # 11 binary
            elsif board[r][c] == 0 && live_neighbors == 3
                board[r][c] = 2 # 10 binary
            end
        end
    end
    
    (0...board.length).each do |r|
        (0...board[0].length).each do |c|
            # get next state from 2nd bit
            board[r][c] = board[r][c] >> 1
        end
    end
      
    return board
end

def get_live_neighbors(board, r, c)
    live_neighbors = 0
    shifts = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    shifts.each do |s_r, s_c|
        if out_of_bounds(r, s_r, c, s_c, board)
            next
        end
        # get current state from 1st bit
        if board[r + s_r][c + s_c] & 1 == 1
            live_neighbors += 1
        end
    end
    
    return live_neighbors
end
    
def out_of_bounds(r, s_r, c, s_c, board)
    r + s_r < 0 || r + s_r >= board.length || c + s_c < 0 || c + s_c >= board[0].length
end