=begin
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
=end

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
    if matrix.empty?
        return false
    end
    
    m = matrix.length
    n = matrix[0].length
    
    lo = 0
    hi = m-1
    
    while lo != hi && matrix[hi][0] > target
        mid = (lo + hi + 1)/2
        if matrix[mid][0] == target
            return true
        elsif matrix[mid][0] < target
            lo = mid
        else
            hi = mid - 1
        end
    end
    
    row = hi
    lo = 0
    hi = n-1
    while lo <= hi
        mid = (lo + hi)/2
        if matrix[row][mid] == target
            return true
        elsif matrix[row][mid] < target
            lo = mid + 1
        else
            hi = mid - 1
        end
    end
    
    return false
end

