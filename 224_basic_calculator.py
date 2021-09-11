'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 

Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        for char in s:
            if char.isdigit():
                num = 10 * num + int(char)
            elif char in ["-", "+"]:
                res += sign * num
                num = 0
                sign = 1 if char == "+" else -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif char == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
                
        return res + num * sign
            
