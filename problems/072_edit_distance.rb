=begin
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
=end

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
    n = word1.length
    m = word2.length
    
    if n == 0 || m == 0
        return n + m
    end
    
    d = Array.new(n+1){Array.new(m+1){0}}
    (0..n).each do |i|
        d[i][0] = i
    end
    (0..m).each do |j|
        d[0][j] = j
    end
    
    (1..n).each do |i|
        (1..m).each do |j|
            if word1[i-1] == word2[j-1]
                d[i][j] = d[i-1][j-1]
            else
                left = d[i-1][j]
                down = d[i][j-1]
                left_down = d[i-1][j-1]
                d[i][j] = 1 + [left, down, left_down].min
            end
        end
    end
    
    return d[n][m]
end

