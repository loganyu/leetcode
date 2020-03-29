=begin
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
=end
# @param {Integer} num
# @return {Integer}
def maximum_swap(num)
    digits = num.to_s
    max = digits[-1]
    l = r = max_i = -1
    (digits.length - 2).downto(0).each do |i|
        if digits[i] > max
            max = digits[i]
            max_i = i
        end
        if digits[i] < max
            l = i
            r = max_i
        end
    end
    if l != -1
        digits[l], digits[r] = digits[r], digits[l]
    end
    
    digits.to_i
end