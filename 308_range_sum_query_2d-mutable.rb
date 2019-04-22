=begin
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
=end

class NumMatrix

=begin
    :type matrix: Integer[][]
=end
    def initialize(matrix)
        if matrix.empty? || matrix[0].empty?
            return 0
        end
        height = matrix.length
        width = matrix[0].length
        @sums = Array.new(height + 1){Array.new(width + 1){0}}
        (0...height).each do |row|
            (0...width).each do |col|
                @sums[row + 1][col + 1] = @sums[row + 1][col] + @sums[row][col + 1] + 
                                            matrix[row][col] - @sums[row][col]
            end
        end
        @matrix = matrix
    end


=begin
    :type row: Integer
    :type col: Integer
    :type val: Integer
    :rtype: Void
=end
    def update(row, col, val)
        delta = val - @matrix[row][col]
        @matrix[row][col] = val
        (row+1...@sums.length).each do |r|
            (col+1...@sums[0].length).each do |c|
                @sums[r][c] += delta
            end
        end
    end


=begin
    :type row1: Integer
    :type col1: Integer
    :type row2: Integer
    :type col2: Integer
    :rtype: Integer
=end
    def sum_region(row1, col1, row2, col2)
        @sums[row2 + 1][col2 + 1] - @sums[row2 + 1][col1] - @sums[row1][col2 + 1] + @sums[row1][col1]
    end


end

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix.new(matrix)
# obj.update(row, col, val)
# param_2 = obj.sum_region(row1, col1, row2, col2)