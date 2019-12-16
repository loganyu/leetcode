=begin
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
=end

require 'set'

# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern(pattern, str)
    words = str.split()
    mapping = {}
    seen = Set.new
    if pattern.length != words.length
        return false
    end
    
    pattern.each_char.with_index do |char, i|
        if mapping[char]
            if mapping[char] != words[i]
                return false
            end
        elsif seen.include?(words[i]) 
            return false
        else
            mapping[char] = words[i]
            seen.add(words[i])
        end
    end
    
    return true
end

