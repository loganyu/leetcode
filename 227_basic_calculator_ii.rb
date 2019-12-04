=begin
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
=end

# @param {String} s
# @return {Integer}
def calculate(s)
    sum = temp_sum = num = 0
    op = '+'
    s += "+0"
    s.each_char do |char|
        if /\d/.match(char)
            num = num * 10 + char.to_i
        elsif ['+', '-', '*', '/'].include?(char)
            if op == '+'
                sum += temp_sum
                temp_sum = num
            elsif op == '-'
                sum += temp_sum
                temp_sum = -num
            elsif op == '*'
                temp_sum *= num
            else
                temp_sum = (temp_sum / num.to_f).truncate
            end
            op, num = char, 0
        end
    end
    sum += temp_sum
    
    return sum
end
