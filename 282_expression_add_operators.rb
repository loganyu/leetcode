=begin
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
=end

# @param {String} num
# @param {Integer} target
# @return {String[]}
def add_operators(num, target)
    @answers = []
    @num = num
    @target = target
    @string = ''
    recurse(0, 0, 0, 0)
    
    return @answers
end

def recurse(i, prev_op, curr_op, val)
    if i == @num.length
        if val == @target && curr_op == 0
            @answers << @string[1..-1]
        end
        return
    end
    curr_op = curr_op*10 + @num[i].to_i
    str_op = curr_op.to_s
    # continue
    if curr_op > 0
        recurse(i+1, prev_op, curr_op, val)
    end
    # add op
    @string.concat('+').concat(str_op)
    recurse(i+1, curr_op, 0, val + curr_op)
    @string.chomp!(str_op).chomp!('+')
    if !@string.empty?
        # substract op
        @string.concat('-').concat(str_op)
        recurse(i+1, -curr_op, 0, val - curr_op)
        @string.chomp!(str_op).chomp!('-')
        # multiply op
        @string.concat('*').concat(str_op)
        recurse(i+1, curr_op * prev_op, 0, val - prev_op + (prev_op * curr_op))
        @string.chomp!(str_op).chomp!('*')
    end
end