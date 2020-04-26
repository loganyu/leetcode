=begin
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false  
=end

# @param {String} s
# @param {String} p
# @return {Boolean}
# recursive solution
def is_match(s, p)
  return s.empty? if p.empty?
  first = !s.empty? && [s[0], '.'].include?(p[0])
  if p[1] == '*'
    is_match(s, p[2..-1]) || (first && is_match(s[1..-1], p))
  else
    first && is_match(s[1..-1], p[1..-1])
  end
end

# recursive with indexes
def is_match_a(i, j, s, p)
  return i == s.length if j == p.length
  first = i < s.length && [s[i], '.'].include?(p[j])
  if p[j+1] == '*'
    is_match_a(i, j+2, s, p) || (first && is_match_a(i+1, j, s, p))
  else
    first && is_match_a(i+1, j+1, s, p)
  end
end

# dynamic programming bottom up
def is_match(s, p)
  dp = Array.new(s.length+1) { Array.new(p.length+1, false) }
  m, n = s.length, p.length
  dp[m][n] = true
  m.downto(0) do |i|
    (n-1).downto(0) do |j| 
      first = i < m && (s[i] == p[j] || p[j] == '.')
      if p[j+1] == '*'
        dp[i][j] = dp[i][j+2] || (first && dp[i+1][j])
      else
        dp[i][j] = first && dp[i+1][j+1]
      end
    end
  end
  dp[0][0]
end
