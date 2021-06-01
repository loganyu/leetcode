=begin
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
=end

# @param {Integer[]} ratings
# @return {Integer}
def candy(ratings)
    n = ratings.length
    left_to_right = Array.new(n){1}
    right_to_left = Array.new(n){1}
    
    (1...n).each do |i|
        if ratings[i] > ratings[i-1]
            left_to_right[i] = left_to_right[i-1] + 1
        end
    end
    (n-2).downto(0).each do |i|
        if ratings[i] > ratings[i+1]
            right_to_left[i] = right_to_left[i+1] + 1
        end
    end
    
    sum = 0
    (0...n).each do |i|
        sum += [left_to_right[i], right_to_left[i]].max
    end
    
    return sum
end

