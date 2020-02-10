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

# O(nm) space
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

# O(n) space
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        max_len = 0
        prev = 0
        dp = [0 for _ in range(cols+1)]
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                temp = dp[c]
                if matrix[r-1][c-1] == '1':
                    dp[c] = min(dp[c-1], dp[c], prev) + 1
                    max_len = max(max_len, dp[c])
                else:
                    dp[c] = 0
                prev = temp
        
        return max_len**2