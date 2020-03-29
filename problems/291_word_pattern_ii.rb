=begin
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.
=end

require 'set'
# @param {String} pattern
# @param {String} str
# @return {Boolean}
def word_pattern_match(pattern, str)
    map = {}
    set = Set.new
    is_match(pattern, str, 0, 0, map, set)
end

def is_match(pattern, str, p, s, map, set)
    if p == pattern.length && s == str.length
        return true
    end
    if p == pattern.length || s == str.length
        return false
    end
    
    char = pattern[p]
    if map[char]
        word = map[char]
        if word != str[s...s+word.length]
            return false
        end
        
        return is_match(pattern, str, p+1, s+word.length, map, set)
    end
    
    (s...str.length).each do |i|
        word = str[s..i]
        if set.include?(word)
            next
        end
        
        map[char] = word
        set.add(word)
        if is_match(pattern, str, p+1, i+1, map, set)
            return true
        end
        map.delete(char)
        set.delete(word)
    end
    
    return false
end

