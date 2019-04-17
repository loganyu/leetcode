=begin
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
=end

# @param {String} s
# @return {Integer}
def num_decodings(s)
    n = s.length
    if n == 0
        return 0
    end
    
    memo = []
    memo[n] = 1
    memo[n-1] = s[n-1] != '0' ? 1 : 0
    
    (n-2).downto(0).each do |i|
       if s[i] == '0'
           memo[i] = 0
       else
           if  (s[i..i+1].between?('1', '26'))
               memo[i] = memo[i+1] + memo[i+2]
           else
               memo[i] = memo[i+1]
           end
       end
    end
    
    return memo[0]    
end
