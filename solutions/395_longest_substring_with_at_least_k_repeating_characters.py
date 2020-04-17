'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        if all(count >= k for _, count in counts.items()):
            return len(s)
        
        excluded = set([char for char, count in counts.items() if count < k])
        
        l = r = 0
        longest = 0
        while r < len(s):
            char = s[r]
            if counts[char] < k:
                longest = max(longest, self.longestSubstring(s[l:r], k))
                l = r + 1
            r += 1
        
        longest = max(longest, self.longestSubstring(s[l:r], k))
        
        return longest

