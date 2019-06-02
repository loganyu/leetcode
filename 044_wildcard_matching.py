'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

# Recursion with memorisation O(min(S,P)),  
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = self.remove_duplicate_stars(p)
        self.dp = {}
        return self.helper(s, p)
        
    def helper(self, s: str, p: str) -> bool:
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        elif p == s or p == '*':
            dp[(s,p)] = True
        elif p == '' or s == '':
            dp[(s,p)] = False
        elif p[0] == s[0] or p[0] == '?':
            dp[(s,p)] = self.helper(s[1:], p[1:])
        elif p[0] == '*':
            dp[(s,p)] = self.helper(s, p[1:]) or self.helper(s[1:], p)
        else:
            dp[(s,p)] = False
            
        return dp[(s,p)]
        
        
    def remove_duplicate_stars(self, p: str) -> str:
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

# DP solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False
        
        d = [ [False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True
        
        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == '*':
                s_idx = 1
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
                
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
            else:
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]
                    

        return d[p_len][s_len]
                
