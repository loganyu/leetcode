=begin
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
=end

# @param {Integer} n
# @return {Integer}
def num_squares(n)
    dp = Array.new(n+1){Float::INFINITY}
    dp[0] = 0
    dp[1] = 1
    (2..n).each do |i|
        (1..(Math.sqrt(i).floor)).each do |j|
            dp[i] = [dp[i], dp[i - j*j] + 1].min
        end
    end
    
    return dp[n]
end