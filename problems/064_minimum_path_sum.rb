=begin
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
=end

# @param {Integer[][]} grid
# @return {Integer}
def min_path_sum(grid)
    h = grid.length
    w = grid[0].length
    dp = Array.new(h){Array.new(w)}
    (h-1).downto(0).each do |i|
        (w-1).downto(0).each do |j|
            if i == h-1 && j != w-1
                dp[i][j] = grid[i][j] + dp[i][j+1]
            elsif i != h-1 && j == w-1
                dp[i][j] = grid[i][j] + dp[i+1][j]
            elsif i != h-1 && j != w-1
                dp[i][j] = grid[i][j] + [dp[i+1][j], dp[i][j+1]].min
            else
                dp[i][j] = grid[i][j]
            end
        end
    end
    
    return dp[0][0]
end

