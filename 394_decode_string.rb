-begin
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
=end

# @param {String} s
# @return {String}
def decode_string(s)
    stack = []
    stack.push(["", 1])
    num = ""
    s.each_char do |char|
       if char =~ /\d/
           num += char
       elsif char == '['
           stack.push(["", num.to_i])
           num = ""
       elsif char == ']'
           st, k = stack.pop
           stack[-1][0] += st*k
       else
           stack[-1][0] += char
       end
    end
    
    return stack[0][0]
end