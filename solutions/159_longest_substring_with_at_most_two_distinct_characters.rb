=begin
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
=end

# @param {String} s
# @return {Integer}
def length_of_longest_substring_two_distinct(s)
    map = {}
    max = 0
    l = r = 0
    while r < s.length
        map[s[r]] = r
        r += 1
        if map.count == 3
            first_char, first_idx = map.min_by{|char, i| i}
            map.delete(first_char)
            l = first_idx + 1
        end
        
        max = [max, r - l].max
    end
    
    return max
end
