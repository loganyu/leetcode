'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = set("AEIOUaeiou")
        word = list(s)
        while l < r:
            while word[l] not in vowels and l < r:
                l += 1
            while word[r] not in vowels and l < r:
                r -= 1
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
            
        return "".join(word)

