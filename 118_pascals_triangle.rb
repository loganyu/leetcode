=begin
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
=end

# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    triangle = []
    (0...num_rows).each do |i|
        row = Array.new(i+1)
        row[0] = row[-1] = 1
        (1...i).each do |j|
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        end
        
        triangle << row
    end
    
    return triangle
end

