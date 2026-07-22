t '''
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.


Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
'''

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        vis = [0] * 26
        num = [0] * 26

        for ch in s:
            num[ord(ch) - ord("a")] += 1
        stk = []

        for ch in s:
            idx = ord(ch) - ord("a")
            if not vis[idx]:
                while stk and stk[-1] > ch:
                    top_idx = ord(stk[-1]) - ord("a")
                    if num[top_idx] > 0:
                        vis[top_idx] = 0
                        stk.pop()
                    else:
                        break
                vis[idx] = 1
                stk.append(ch)
            num[idx] -= 1

        return "".join(stk)

