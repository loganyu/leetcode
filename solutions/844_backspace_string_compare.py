'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''
# O(1) space
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        si = len(S) - 1
        ti = len(T) - 1
        while si >= 0 or ti >= 0:
            s_char, si = self.get_char_and_next_index(si, S)
            t_char, ti = self.get_char_and_next_index(ti, T)
            if s_char != t_char:
                return False
        return True
    
    def get_char_and_next_index(self, i, string):
        char = ""
        count = 0
        while i >= 0 and not char:
            if string[i] == "#":
                count += 1
            elif count > 0:
                count -= 1
            else:
                char = string[i]
            i -= 1
            
        return char, i 

# O(n+m) space
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        for char in S:
            if char != '#':
                s_stack.append(char)
            elif s_stack:
                s_stack.pop()
        for char in T:
            if char != '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()
        return s_stack == t_stack
        
