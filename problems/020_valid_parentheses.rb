=begin
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
=end

# @param {String} s
# @return {Boolean}
def is_valid(s)
    stack = []
    mapping = {
        ')' => '(',
        '}' => '{',
        ']' => '[',
    }
    
    s.each_char do |char|
        if mapping[char]
            if !stack.empty?
                top_element = stack.pop
            end
            if mapping[char] != top_element
                return false
            end
        else
            stack.push(char)
        end
    end
    
    return stack.empty?
end