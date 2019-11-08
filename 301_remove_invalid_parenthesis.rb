=begin
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
=end

require 'set'

# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    left_rem = 0
    right_rem = 0
    s.each_char do |char|
        if char == '('
            left_rem += 1
        elsif char == ')'
            if left_rem == 0
                right_rem += 1
            else
                left_rem -= 1
            end
        end
    end
    result = Set.new
    recurse(s, 0, 0, 0, left_rem, right_rem, [], result)
    
    return result.to_a
end

def recurse(s, index, left_count, right_count, left_rem, right_rem, expr, result)
    if index == s.length
        if left_rem == 0 && right_rem == 0
            result.add(expr.join)
        end
    else
        # discard case
        if (s[index] == '(' && left_rem > 0) || (s[index] == ')' && right_rem > 0)
            recurse(s, index + 1, left_count, right_count, left_rem - (s[index] == '(' ? 1 : 0), right_rem - (s[index] == ')' ? 1 : 0), expr, result)
        end
        expr << s[index]
        if s[index] != '(' && s[index] != ')'
            recurse(s, index + 1, left_count, right_count, left_rem, right_rem, expr, result)
        elsif s[index] == '('
            recurse(s, index + 1, left_count + 1, right_count, left_rem, right_rem, expr, result)
        elsif s[index] == ')' && left_count > right_count
            recurse(s, index + 1, left_count, right_count + 1, left_rem, right_rem, expr, result)
        end
        
        expr.pop()
    end
end
