=begin
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
=end

# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
    seen = {}
    back_idx = 0
    max_count = 0
    
    (0..s.size - 1).each do |idx|
        letter = s[idx]
        if !seen[letter].nil? && seen[letter] >= back_idx
            current_count = idx - back_idx
            max_count = [max_count, current_count].max
            back_idx = seen[letter] + 1
        end
        seen[letter] = idx
    end
    
    current_count = s.size - back_idx
    [max_count, current_count].max
end