=begin
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
=end

# @param {String} s
# @return {String}
# dp solution time limit gets exceeded in leetcode
def longest_palindrome_by_dynamic_programming(s1)
  s2 = s1.reverse
  t = Array.new(s1.length + 1) {Array.new(s2.length + 1) {0}}
  max = 0
  max_substring = ""
  1.upto(s1.length).each do |i|
    1.upto(s2.length).each do |j|
      if s1[i-1] == s2[j-1]
        t[i][j] = t[i-1][j-1] + 1
        if max < t[i][j]
          s1_substring_start = i - t[i][j]
          s2_pos_orig = s2.length - 1 - (j - 1)
          if s1_substring_start == s2_pos_orig
            max = t[i][j]
            max_substring = s1[s1_substring_start...i]
          end
        end
      end
    end
  end
  max_substring
end

def longest_palindrome_by_expanding(s)
    max_indexes = [0, 0]
    
    (0..(s.size - 1)).each do |idx|
        start_1, end_1 = expand_palindrome(idx, idx, s)
        start_2, end_2 = expand_palindrome(idx, idx + 1, s)
        
        if end_1 - start_1 > max_indexes[1] - max_indexes[0]
            max_indexes = [start_1, end_1]
        end
        
        if end_2 - start_2 > max_indexes[1] - max_indexes[0]
            max_indexes = [start_2, end_2]
        end
    end
    
    s[max_indexes[0]..max_indexes[1]]
end

def expand_palindrome(start_idx, end_idx, s)
    while start_idx >= 0 && end_idx <= s.size - 1 && s[start_idx] == s[end_idx]
        start_idx -= 1
        end_idx += 1
    end
    
    return start_idx + 1, end_idx - 1
end
