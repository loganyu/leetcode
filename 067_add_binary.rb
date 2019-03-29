=begin
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
=end

# @param {String} a
# @param {String} b
# @return {String}
def add_binary(a, b)
    ai = a.length - 1
    bi = b.length - 1
    carry_over = 0
    sol = ''
    while (ai >= 0 || bi >=0 || carry_over > 0)
        sum = carry_over
        if ai >= 0
            sum += a[ai].to_i
        end
        if bi >= 0
            sum += b[bi].to_i
        end
        carry_over = sum / 2
        sol = (sum % 2).to_s + sol
        
        ai -= 1
        bi -= 1
    end
    
    sol
end