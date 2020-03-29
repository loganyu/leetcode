'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = right = n
        sol = []
        self.backtrack(sol, left, right, n, "")
        
        return sol
    
    def backtrack(self, sol, left, right, n, combo):
        if len(combo) == 2*n:
            sol.append(combo)
            return
        if left > 0:
            self.backtrack(sol, left - 1, right, n, combo + '(')
        if right > left:
            self.backtrack(sol, left, right - 1, n, combo + ')')
        
