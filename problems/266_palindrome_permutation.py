'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        odd_chars = set()
        for char in s:
            if char not in odd_chars:
                odd_chars.add(char)
            else:
                odd_chars.remove(char)
        
        return len(odd_chars) <= 1;
        
