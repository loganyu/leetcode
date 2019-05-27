=begin
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
=end

# @param {String} s
# @param {Integer} k
# @return {Integer}
def length_of_longest_substring_k_distinct(s, k)
    map = {}
    max = 0
    l = r = 0
    while r < s.length
        map[s[r]] = r
        r += 1
        if map.count == k+1
            first_char, first_idx = map.min_by{|char, i| i}
            map.delete(first_char)
            l = first_idx + 1
        end
        
        max = [max, r - l].max
    end
    
    return max
end

