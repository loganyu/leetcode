'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_by_char = defaultdict(int)
        for char in s:
            count_by_char[char] += 1
        for i, char in enumerate(s):
            if count_by_char[char] == 1:
                return i
        return -1

