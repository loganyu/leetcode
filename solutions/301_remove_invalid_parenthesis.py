'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left_rem = 0
        right_rem = 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem == 0:
                    right_rem += 1
                else:
                    left_rem -= 1
        
        result = set()
        self.recurse(s, 0, 0, 0, left_rem, right_rem, [], result)
        
        return list(result)
    
    def recurse(self, s, i, left_count, right_count, left_rem, right_rem, expr, result):
        if i == len(s):
            if left_rem == 0 and right_rem == 0:
                result.add("".join(expr))
        else:
            if s[i] == '(':
                if left_rem > 0:
                    self.recurse(s, i+1, left_count, right_count, left_rem - 1, right_rem, expr, result)
                expr.append('(')
                self.recurse(s, i+1, left_count + 1, right_count, left_rem, right_rem, expr, result)
                expr.pop()
            elif s[i] == ')':
                if right_rem > 0:
                    self.recurse(s, i+1, left_count, right_count, left_rem, right_rem - 1, expr, result)
                if left_count > right_count:
                    expr.append(')')
                    self.recurse(s, i+1, left_count, right_count + 1, left_rem, right_rem, expr, result)
                    expr.pop()
            else:
                expr.append(s[i])
                self.recurse(s, i+1, left_count, right_count, left_rem, right_rem, expr, result)
                expr.pop()
        
