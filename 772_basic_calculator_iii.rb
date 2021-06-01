=begin
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, / operators , open ( and closing parentheses ) and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:

"1 + 1" = 2
" 6-4 / 2 " = 4
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12
 

Note: Do not use the eval built-in library function.
=end

# @param {String} s
# @return {Integer}
def calculate(s)
    nums, ops = [], []
    i = 0
    while i < s.length
        char = s[i]
        if /\d/.match(char)
            num = char.to_i
            while i < s.length && /\d/.match(s[i+1])
                num = num * 10 + s[i+1].to_i
                i += 1
            end
            nums << num
        elsif char == '('
            ops << char
        elsif char == ')'
            while ops[-1] != '('
                nums << operate(ops.pop, nums.pop, nums.pop)
            end
            ops.pop
        elsif ['+', '-', '*', '/'].include?(char)
            while ops.length > 0 && should_operate?(ops[-1], char)
                nums << operate(ops.pop, nums.pop, nums.pop)
            end
            ops << char
        end
        i += 1
    end
    
    while ops.length > 0
        nums << operate(ops.pop, nums.pop, nums.pop)
    end
    
    return nums.pop
end
    
def operate(op, second, first)
    case op
    when "+"
        return first + second
    when "-"
        return first - second
    when "*"
        return first * second
    when "/"
        return first / second
    end
end

def should_operate?(op, next_op)
    if ['(', ')'].include?(op)
        return false
    end
    if ['*','/'].include?(next_op) && ['+','-'].include?(op)
        return false
    end
    return true
end

