=begin
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
=end

# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    l = 0
    r = s.length - 1
    while l < r
        while !s[l].match(/[a-zA-Z0-9]/) && l < r
            l += 1
        end
        while !s[r].match(/[a-zA-Z0-9]/) && l < r
            r -= 1
        end
        if s[l].downcase != s[r].downcase
            return false
        end
        l += 1
        r -= 1
    end
    
    return true
end
