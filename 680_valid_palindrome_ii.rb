=begin
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
=end

# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
    0.upto(s.length/2-1).each do |i|
        if s[i] != s[~i]
            j = s.length - 1 - i
            return is_pali_range(s, i+1, j) || is_pali_range(s, i, j-1)
        end
    end
    
    return true
end

def is_pali_range(s, i, j)
   i.upto(j-1).each do |k|
      if s[k] != s[j-k+i]
          return false
      end
   end
    
    return true
end