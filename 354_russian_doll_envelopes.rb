=begin
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
=end

# TLE O(n^2) runtime
# @param {Integer[][]} envelopes
# @return {Integer}
def max_envelopes(envelopes)
    if envelopes.empty?
        return 0
    end
    envelopes.sort_by!{|h,w| [h, -w]}
    n = envelopes.length
    max_ans = 1
    dp = []
    dp[0] = 1
    
    (0...n).each do |i|
        max_env = 0
        (0...i).each do |j|
            if envelopes[j][0] < envelopes[i][0] && envelopes[j][1] < envelopes[i][1]
                max_env = [max_env, dp[j]].max
            end
        end
        dp[i] = max_env + 1
        max_ans = [max_ans, dp[i]].max
    end
    
    return max_ans
end

# O(n logn) runtime
# @param {Integer[][]} envelopes
# @return {Integer}
def max_envelopes(envelopes)
    if envelopes.empty?
        return 0
    end
    envelopes.sort_by!{|h,w| [h, -w]}
    
    dp = []
    
    envelopes.each do |envelope|
        i = 0
        j = dp.length
        while i != j
            m = i + (j-i)/2
            if dp[m][0] < envelope[0] && dp[m][1] < envelope[1]
                i = m + 1
            else
                j = m
            end
        end
        dp[i] = envelope
    end
    
    return dp.length
end
