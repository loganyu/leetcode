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
    stack, num, op = [], 0, "+"
    s += "+0"
    s.each_char do |char|
        if /\d/.match(char)
            num = num * 10 + char.to_i
        elsif ['+', '-', '*', '/'].include?(char)
            if op == '-'
                stack.push(-num)
            elsif op == '+'
                stack.push(num)
            elsif op == '*'
                stack.push(stack.pop() * num)
            else
                num2 = stack.pop()
                if num2/num < 0 && num2%num != 0
                    stack.push(num2/num+1)
                else
                    stack.push(num2/num)
                end
            end
            op, num = char, 0
        end
    end
    
    stack.sum
end


puts calculate("14-3/2")