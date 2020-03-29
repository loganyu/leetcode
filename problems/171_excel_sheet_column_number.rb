=begin
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
=end

# @param {String} s
# @return {Integer}
def title_to_number(s)
    length = s.length
    num = 0
    s.each_char.with_index do |char, i|
        num = num * 26 + (char.ord - 'A'.ord + 1)
    end
    
    return num
end

