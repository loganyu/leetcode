=begin
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
=end

# @param {Integer} num
# @return {Boolean}
def is_power_of_four(num)
    num > 0 && num.to_s(2).count('1') == 1 && (num.to_s(2).length - 1) % 2 == 0
end

def is_power_of_four(num)
    while num > 1
        if num % 4 != 0
            return false
        end
        num /= 4
    end
    
    num == 1
end

