=begin
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
=end

# @param {Integer[]} coins
# @param {Integer} amount
# @return {Integer}
def coin_change(coins, amount)
    if amount < 1
        return 0
    end
    dp = Array.new(amount + 1){Float::INFINITY}
    dp[0] = 0
    1.upto(amount) do |i|
        0.upto(coins.length - 1).each do |j|
            if coins[j] <= i
                dp[i] = [dp[i], dp[i - coins[j]] + 1].min
            end
        end
    end
    
    return dp[amount] == Float::INFINITY ? -1 : dp[amount]
end
