=begin
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
=end

# @param {Integer[][]} matrix
# @return {Integer[]}
def find_diagonal_order(matrix)
    sol = []
    m = matrix.length
    if m == 0
        return sol
    end
    n = matrix[0].length
    r = 0
    c = 0
    d = 1
    
    (n*m).times do
        sol << matrix[r][c]
        r -= d
        c += d
        
        if r >= m
            r = m - 1
            c += 2
            d = -d
        elsif c >= n
            c = n - 1
            r += 2
            d = -d
        elsif r < 0
            r = 0
            d = -d
        elsif c < 0
            c = 0
            d = -d
        end
    end
    
    return sol
end

