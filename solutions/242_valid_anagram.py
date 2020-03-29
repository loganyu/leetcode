'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_by_letter = Counter()
        for char in s:
            count_by_letter[char] += 1
        for char in t:
            if char not in count_by_letter:
                return False
            count_by_letter[char] -= 1
            if count_by_letter[char] < 0:
                return False
        
        return True
        
