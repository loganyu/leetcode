=begin
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
=end

# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
    if num_rows == 1
        return s
    end
    rows = Array.new(num_rows){''}
    row = 0
    delta = -1
    s.each_char do |char|
        rows[row] += char
        if row == 0 || row == num_rows - 1
            delta *= -1
        end 
        row += delta
    end

    rows.join
end
