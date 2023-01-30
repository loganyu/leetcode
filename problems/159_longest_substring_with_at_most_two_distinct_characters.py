'''
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        last_index_by_char = OrderedDict()
        longest = 0
        l = r = 0
        while r < len(s):
            char = s[r]
            if char in last_index_by_char:
                del last_index_by_char[char]
            last_index_by_char[char] = r
            r += 1
            if len(last_index_by_char) > 2:
                _, del_idx = last_index_by_char.popitem(last = False)
                l = del_idx + 1
            longest = max(longest, r-l)
        
        return longest

