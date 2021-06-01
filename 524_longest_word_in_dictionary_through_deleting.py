'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest_word = ""
        for word in d:
            if self.isSubsequence(word, s):
                if len(word) > len(longest_word) or len(word) == len(longest_word) and word < longest_word:
                    longest_word = word
        
        return longest_word
    
    def isSubsequence(self, word, s):
        i = 0
        j = 0
        while i < len(word) and j < len(s):
            if word[i] == s[j]:
                i += 1
            j += 1 
        return i == len(word)
        
