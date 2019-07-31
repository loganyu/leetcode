=begin
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
=end

# @param {String} s
# @return {Integer}
def length_of_last_word(s)
    len = 0
    tail = s.length - 1
    while tail >= 0 && s[tail] == ' '
        tail -= 1
    end
    while tail >= 0 && s[tail] != ' '
        len += 1
        tail -= 1
    end
    
    return len
end

