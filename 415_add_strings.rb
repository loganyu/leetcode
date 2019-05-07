=begin
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

=end

# @param {String} num1
# @param {String} num2
# @return {String}
def add_strings(num1, num2)
    i = num1.length - 1
    j = num2.length - 1
    sol = ''
    carry = 0
    while i >= 0 || j >= 0 || carry > 0
        sum = carry
        if i >= 0
            sum += num1[i].ord - '0'.ord
            i -= 1
        end
        if j >= 0
            sum += num2[j].ord - '0'.ord
            j -= 1
        end
        carry = sum/10
        sol = String(sum%10) + sol
    end
    
    sol
end

