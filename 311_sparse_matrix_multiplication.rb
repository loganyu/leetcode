=begin
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
=end

# @param {Integer[][]} a
# @param {Integer[][]} b
# @return {Integer[][]}
def multiply(a, b)
    sol = Array.new(a.length){Array.new(b[0].length){0}}
    0.upto(sol.length - 1).each do |row|
        0.upto(a[0].length - 1).each do |i|
            if a[row][i] != 0
                0.upto(sol[0].length - 1).each do |col|
                    sol[row][col] += a[row][i] * b[i][col]
                end
            end
        end
    end
    
    return sol
end