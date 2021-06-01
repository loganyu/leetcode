'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        
        ns, nt = len(s), len(t) 
        if ns > nt:
            s, t = t, s
            ns, nt = nt, ns
        
        if nt - ns > 1:
            return False
        
        si, ti = 0, 0
        diff_found = False
        while si < ns and  ti < nt:
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                if diff_found:
                    return False
                diff_found = True
                if ns < nt:
                    ti += 1
                else:
                    si += 1
                    ti += 1
        return True

