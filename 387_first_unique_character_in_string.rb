=begin
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
=end

# @param {String} s
# @return {Integer}
def first_uniq_char(s)
    count_by_letter = {}
    s.each_char do |char|
        count_by_letter[char] ||= 0
        count_by_letter[char] += 1
    end
    s.each_char.with_index do |char, index|
        if count_by_letter[char] == 1
            return index
        end
    end
    
    return -1
end