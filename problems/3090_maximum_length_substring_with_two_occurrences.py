'''
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.


Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = [0] * 26
        left = 0
        res = 0
        for right, c in enumerate(s):
            ch = ord(c) - ord("a")
            count[ch] += 1
            while count[ch] > 2:
                ch2 = ord(s[left]) - ord("a")
                count[ch2] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        
