=begin
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
=end

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    if prices.length < 2
        return 0
    end
    sell = 0
    prev_sell = 0
    buy = -prices[0]
    prev_buy = 0
    prices.each do |price|
        prev_buy = buy
        buy = [prev_sell - price, prev_buy].max
        prev_sell = sell
        sell = [prev_buy + price, prev_sell].max
    end
    
    return sell
end

