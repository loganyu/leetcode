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
    if n == 0 || s[0] == '0'
        return 0
    end
    
    curr = prev = 1
    (1...n).each do |i|
        if s[i] == '0'
            curr = 0
        end
        if s[i-1..i].between?('1', '26')
            curr = curr + prev
            prev = curr - prev
        else
            prev = curr
        end
    end
    
    return curr
end
