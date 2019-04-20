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
    s = s.gsub(/[^a-zA-Z\d]/, "").downcase
    0.upto(s.length/2-1).each do |i|
        if s[i] != s[~i]
            return false
        end
    end
    
    return true
end