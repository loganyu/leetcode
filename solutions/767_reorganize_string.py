'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
'''

class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        a = []
        for count, char in sorted((S.count(char), char) for char in set(S)):
            if count > (n + 1) / 2:
                return ""
            a.extend(count * char)
        ans = [None] * n
        ans[::2], ans[1::2] = a[n//2:], a[:n//2]
        
        return "".join(ans)

