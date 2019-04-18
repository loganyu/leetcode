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
    answers = []
    recurse(0, 0, 0, 0, "", num, target, answers)
    
    return answers
end

def recurse(index, prev_operand, current_operand, value, string, num, target, answers)
    if index == num.length
        if value == target && current_operand == 0
            answers << string[1..-1]
        end
        return
    end
    
    current_operand = current_operand*10 + num[index].to_i
    str_op = current_operand.to_s
    
    if current_operand > 0
        recurse(index + 1, prev_operand, current_operand, value, string, num, target, answers)
    end
    string.concat('+').concat(str_op)
    recurse(index + 1, current_operand, 0, value + current_operand, string, num, target, answers)
    string.chomp!(str_op).chomp!('+')
    if !string.empty?
        string.concat('-').concat(str_op)
        recurse(index + 1, -current_operand, 0, value - current_operand, string, num, target, answers)
        string.chomp!(str_op).chomp!('-')
        
        string.concat('*').concat(str_op)
        recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string, num, target, answers)
        string.chomp!(str_op).chomp!('*')
    end
end