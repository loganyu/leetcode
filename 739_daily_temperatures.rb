=begin
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
=end

# @param {Integer[]} t
# @return {Integer[]}
def daily_temperatures(t)
    ans = Array.new(t.length){0}
    next_t = Array.new(101){Float::INFINITY}
    (t.length-1).downto(0).each do |i|
        warmer_index = Float::INFINITY
        (t[i]+1).upto(100).each do |t|
            if next_t[t] < warmer_index
                warmer_index = next_t[t]
            end
        end
        if warmer_index < Float::INFINITY
            ans[i] = warmer_index - i
        end
        next_t[t[i]] = i
    end
    
    ans
end
# @param {Integer[]} t
# @return {Integer[]}
def daily_temperatures(t)
    ans = Array.new(t.length){0}
    stack = []
    (t.length-1).downto(0).each do |i|
        while !stack.empty? && t[i] >= t[stack[-1]]
            stack.pop
        end
        ans[i] = stack.empty? ? 0 : stack[-1] - i
        stack.push(i)
    end
    
    ans
end

# def daily_temperatures(t)
#     ans = Array.new(t.length){0}
#     next_t = Array.new(101){Float::INFINITY}
#     (t.length-1).downto(0).each do |i|
#         warmer_index = Float::INFINITY
#         (t[i]+1).upto(100).each do |t|
#             if next_t[t] < warmer_index
#                 warmer_index = next_t[t]
#             end
#         end
#         if warmer_index < Float::INFINITY
#             ans[i] = warmer_index - i
#         end
#         next_t[t[i]] = i
#     end
    
#     ans
# end
