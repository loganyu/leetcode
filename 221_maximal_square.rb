=begin
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
=end

# @param {Character[][]} matrix
# @return {Integer}
def maximal_square(matrix)
    if matrix.empty?
        return 0
    end
    rows = matrix.length
    cols = matrix[0].length
    dp = Array.new(cols+1){0}
    maxsqlen = 0
    prev = 0
    (1..rows).each do |i|
        (1..cols).each do |j|
            temp = dp[j]
            if matrix[i-1][j-1] == '1'
                dp[j] = [dp[j-1], prev, dp[j]].min + 1
                maxsqlen = [maxsqlen, dp[j]].max
            else
                dp[j] = 0
            end
            prev = temp
        end
    end
    
    maxsqlen**2
end

