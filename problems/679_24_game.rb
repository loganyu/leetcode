=begin
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
=end

# @param {Integer[]} nums
# @return {Boolean}
def judge_point24(nums)
    if nums.empty?
        return false
    end
    
    if nums.length == 1
        return (nums[0]-24).abs < 10**-6
    end
    (0...nums.length).each do |i|
        (0...nums.length).each do |j|
            if i != j
                (0...nums.length).each do |k|
                    next_nums = nums.select.with_index{|num,k| ![i,j].include?(k)}
                    ['+', '-', '/', '*'].each do |op|
                        if ['+','*'].include?(op) && j > i
                            next
                        end
                        if op != '/' || nums[j] != 0
                            next_nums << nums[i].send(op, nums[j].to_f)
                            if judge_point24(next_nums)
                                return true
                            end
                            next_nums.pop
                        end
                    end
                end
            end
        end
    end
    
    return false
end

