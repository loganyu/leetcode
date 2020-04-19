'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter()
        n_s1 = len(s1)
        n_s2 = len(s2)
        i = 0
        for i in range(n_s2):
            s2_count[s2[i]] += 1
            if i >= n_s1:
                if s2_count[s2[i - n_s1]] == 1:
                    del s2_count[s2[i - n_s1]]
                else:
                    s2_count[s2[i - n_s1]] -= 1
            
            if s1_count == s2_count:
                return True
        
        return False

