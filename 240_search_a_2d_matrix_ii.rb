=begin
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
=end

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  if matrix.length == 0 || matrix[0].length == 0
      return false
  end
  width = matrix[0].length - 1
  height = matrix.length - 1
  c = 0
  r = height
  loop do
    cur = matrix[r][c]
    if cur == target
      return true
    elsif cur < target
      c = c + 1
    elsif cur > target
      r = r - 1
    end

    if r < 0 || c > width
      return false
    end
  end
end

