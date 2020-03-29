=begin
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
=end

# @param {Integer[][]} m
# @return {Integer}
def longest_line(m)
    if m.empty?
        return 0
    end
    height = m.length
    width = m[0].length
    max = 0
    dp = Array.new(height){Array.new(width)}
    (0...height).each do |r|
        (0...width).each do |c|
            if m[r][c] == 0
                dp[r][c] = [0,0,0,0]
                next
            end
            dp[r][c] = [1,1,1,1]
            dp[r][c][0] += dp[r][c-1][0] if c > 0
            dp[r][c][1] += dp[r-1][c][1] if r > 0
            dp[r][c][2] += dp[r-1][c-1][2] if r > 0 && c > 0
            dp[r][c][3] += dp[r-1][c+1][3] if r > 0 && c < width - 1
            max = ([max] + dp[r][c]).max
        end
    end
    
    return max
end

# @param {Integer[][]} m
# @return {Integer}
def longest_line(m)
    if m.empty?
        return 0
    end
    height = m.length
    width = m[0].length
    max = 0
    col = Array.new(width){0}
    diag = Array.new(width + height){0}
    anti = Array.new(width + height){0}
    (0...height).each do |r|
        row = 0
        (0...width).each do |c|
            if m[r][c] == 1
                row += 1
                col[c] += 1
                diag[c-r+height] += 1
                anti[c+r] += 1
                max = [max, row, col[c], diag[c-r+height], anti[c+r]].max
            else
                row = 0
                col[c] = 0
                diag[c-r+height] = 0
                anti[c+r] = 0
            end
        end
    end
    
    return max
end

