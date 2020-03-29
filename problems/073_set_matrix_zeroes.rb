=begin
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
=end

# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def set_zeroes(matrix)
    is_col = false
    r = matrix.length
    c = matrix[0].length
    (0...r).each do |i|
        if matrix[i][0] == 0
            is_col = true
        end
        (1...c).each do |j|
            if matrix[i][j] == 0
                matrix[0][j] = 0
                matrix[i][0] = 0
            end
        end
    end
    
    (1...r).each do |i|
        (1...c).each do |j|
            if matrix[i][0] == 0 || matrix[0][j] == 0
                matrix[i][j] = 0
            end
        end
    end
    
    if matrix[0][0] == 0
        (0...c).each do |j|
            matrix[0][j] = 0
        end
    end
    
    if is_col
        (0...r).each do |i|
            matrix[i][0] = 0
        end
    end
    
    return matrix
end

