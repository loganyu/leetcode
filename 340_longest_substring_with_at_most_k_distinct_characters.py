'''
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''

from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        last_index_by_char = OrderedDict()
        longest = 0
        l = r = 0
        while r < len(s):
            char = s[r]
            if char in last_index_by_char:
                del last_index_by_char[char]
            last_index_by_char[char] = r
            r += 1
            if len(last_index_by_char) > k:
                _, del_idx = last_index_by_char.popitem(last = False)
                l = del_idx + 1
            longest = max(longest, r-l)
        
        return longest

