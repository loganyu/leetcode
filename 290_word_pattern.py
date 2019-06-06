'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split(' ')
        seen = set()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            if char in mapping:
                if mapping[char] != words[i]:
                    return False
            elif words[i] in seen:
                return False
            else:
                mapping[char] = words[i]
                seen.add(words[i])
        
        return True
