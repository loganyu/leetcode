=begin
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
=end

# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
    dp = Array.new(n+1){0}
    count = 0
    # 0 == invalid
    # 1 == rotatable
    # 2 == valid
    (0..n).each do |num|
        if num < 10
            if [0, 1, 8].include?(num)
                dp[num] = 1
            elsif [2, 5, 6, 9].include?(num)
                dp[num] = 2
                count += 1
            end
        else
            a = num / 10
            b = num % 10
            if dp[a] == 1 && dp[b] == 1
                dp[num] = 1
            elsif dp[a] >= 1 && dp[b] >= 1
                dp[num] = 2
                count += 1
            end
        end
    end
    
    return count
end

# @param {Integer} n
# @return {Integer}
def rotated_digits(n)
    count = 0
    ('0'..n.to_s).each do |num|
        if num.to_s !~ /[347]/ && num.to_s =~ /[2569]/
            count += 1
        end
    end
    
    return count
end
