'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        op = '+'
        s += "+0"
        for c in s:
            if c.isdigit():                    
                num = num*10 + int(c)
            elif c in "+-*/":
                if op == '-':
                    stack.append(-num)
                elif op == '+':
                    stack.append(num)
                elif op == '*':
                    prevNum = stack.pop()
                    newNum = prevNum*num
                    stack.append(newNum)
                elif op == '/':
                    prevNum = stack.pop()
                    if prevNum//num < 0 and prevNum%num != 0:
                        stack.append(prevNum//num+1)
                    else:
                        stack.append(prevNum//num)
                op = c
                num = 0
                
        return sum(stack)

