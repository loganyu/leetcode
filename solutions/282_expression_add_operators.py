'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        self.answers = []
        self.num = num
        self.target = target
        self.string = []
        
        self.recurse(0, 0, 0, 0)
        
        return self.answers
    
    def recurse(self, i, prev_op, curr_op, val):
        if i == len(self.num):
            if val == self.target and curr_op == 0:
                self.answers.append("".join(self.string[1:]))
            return
        curr_op = curr_op * 10 + int(self.num[i])
        str_op = str(curr_op)
        if curr_op > 0:
            self.recurse(i+1, prev_op, curr_op, val)
        
        self.string.append('+')
        self.string.append(str_op)
        self.recurse(i+1, curr_op, 0, val + curr_op)
        self.string.pop()
        self.string.pop()
        
        if self.string:
            self.string.append('-')
            self.string.append(str_op)
            self.recurse(i+1, -curr_op, 0, val - curr_op)
            self.string.pop()
            self.string.pop()
            
            self.string.append('*')
            self.string.append(str_op)
            self.recurse(i+1, prev_op * curr_op, 0, val - prev_op + (prev_op * curr_op))
            self.string.pop()
            self.string.pop()
        
