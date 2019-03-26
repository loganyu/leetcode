=begin
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
=end

# @param {String} s
# @return {Integer}
def calculate(s)
    tokens = tokenize(s)
    
    stack = []
    tokens.each do |token|
        process(stack, token)
    end
    
    stack.first
end

def tokenize(s)
    chars = s.gsub(/\s+/, '').split('')
    chars.reduce([]) do |accum, char|
        if char =~ /\d/
            if accum.last.is_a?(Fixnum)
                accum.push(accum.pop * 10 + char.to_i)
            else
                accum.push(char.to_i)
            end
        else
            accum.push(char)
        end
    end
end
          
def process(stack, token)
   case token
   when '+', '-', '('
       stack.push(token)
   when ')'
       prev_token = stack.pop
       b = stack.pop
       process(stack, prev_token)
   when Fixnum
       if ['+', '-'].include?(stack.last)
           op = stack.pop
           v1 = stack.pop
           v2 = token
           
           res = v1.send(op, v2)
           stack.push(res)
       else
           stack.push(token)
       end
   end
end
       