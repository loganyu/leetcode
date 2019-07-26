=begin
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
=end

# @param {Integer} m
# @param {Integer} n
# @return {Integer}
# O(n) space
def unique_paths(m, n)
    cur = Array.new(n){1}
    (m-1).times do
        (1...n).each do |c|
            cur[c] += cur[c-1]
        end
    end
    
    return cur[n-1]
end

# O(n*m) space
def unique_paths(m, n)
    dp = Array.new(m){Array.new(n)}
    m.times do |i|
        dp[i][0] = 1
    end
    n.times do |i|
        dp[0][i] = 1
    end
    (1...m).each do |r|
        (1...n).each do |c|
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
        end
    end
    
    return dp[m-1][n-1]
end

