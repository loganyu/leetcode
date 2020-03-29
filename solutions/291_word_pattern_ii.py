"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.
"""

class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        wordByChar = {}
        seen = set()
        return self.isMatch(0, 0, pattern, str, wordByChar, seen)
    
    def isMatch(self, p, s, pattern, str, wordByChar, seen):
        if len(pattern) == p and len(str) == s:
            return True
        if len(pattern) == p or len(str) == s:
            return False
        char = pattern[p]
        if char in wordByChar:
            word = wordByChar[char]
            if word != str[s:s+len(word)]:
                return False
            
            return self.isMatch(p+1, s+len(word), pattern, str, wordByChar, seen)
        
        for i in range(s, len(str)):
            word = str[s:i+1]
            if word in seen:
                continue
            wordByChar[char] = word
            seen.add(word)
            if self.isMatch(p+1, i+1, pattern, str, wordByChar, seen):
                return True
            del wordByChar[char]
            seen.remove(word)
        
        return False
        
