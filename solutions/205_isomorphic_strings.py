'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] in used:
                    return False
                mapping[s[i]] = t[i]
                used.add(t[i])
            elif mapping[s[i]] != t[i]:
                return False
        
        return True
    
