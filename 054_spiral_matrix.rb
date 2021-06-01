=begin
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
=end

# @param {Integer[][]} matrix
# @return {Integer[]}
def spiral_order(matrix)
    if matrix.empty?
        return []
    end
    rows = matrix.length
    cols = matrix[0].length
    elements = []
    seen = Array.new(rows){Array.new(cols){false}}
    dir_r = [0,1,0,-1]
    dir_c = [1,0,-1,0]
    dir = 0
    r = 0
    c = 0
    
    (rows*cols).times do
        elements << matrix[r][c]
        seen[r][c] = true
        cr = r + dir_r[dir]
        cc = c + dir_c[dir]
        if 0 <= cr && cr < rows && 0 <= cc && cc < cols && !seen[cr][cc]
            r = cr
            c = cc
        else
            dir = (dir + 1) % 4
            r += dir_r[dir]
            c += dir_c[dir]
        end
    end
    
    return elements
end

