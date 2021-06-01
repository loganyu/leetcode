=begin
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
=end

# @param {String} num1
# @param {String} num2
# @return {String}
def multiply(num1, num2)
    n = num1.length
    m = num2.length
    solution = Array.new(n+m){0}
    
    (n - 1).downto(0).each do |i|
        (m - 1).downto(0).each do |j|
            product = (num1[i].ord - '0'.ord) * (num2[j].ord - '0'.ord)
            p1 = i+j
            p2 = i+j+1
            solution[p2] += product
            solution[p1] += solution[p2] / 10
            solution[p2] %= 10
        end
    end

    while solution.length > 1 && solution[0] == 0
        solution.shift()
    end
    
    solution.join
end