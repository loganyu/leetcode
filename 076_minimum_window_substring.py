'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        l = r = 0
        window_counts = Counter()
        # ans [window length, left, right]
        ans = -1, 0, 0
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            while (l <= r and formed == required):
                if ans[0] == -1 or (r-l+1) < ans[0]:
                    ans = ((r-l+1), l, r)
                char = s[l]
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            r += 1
            
        if ans[0] == -1:
            return ""
        
        return s[ans[1]:ans[2]+1]
                
