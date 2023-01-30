=begin
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
=end

# @param {Integer} row_index
# @return {Integer[]}
def get_row(row_index)
    row = []
    (0..row_index).each do |i|
        row.unshift(1)
        (1...i).each do |j|
            row[j] = row[j] + row[j+1]
        end
    end
    
    return row
end

