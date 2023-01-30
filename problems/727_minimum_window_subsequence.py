'''
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
 

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
'''

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m = len(T)
        n = len(S)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for c in range(n+1):
            dp[0][c] = c + 1
        for r in range(1, m+1):
            for c in range(1, n+1):
                if T[r-1] == S[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = dp[r][c-1]
                    
        start = 0
        length = n + 1
        for c in range(1, n+1):
            if dp[m][c] != 0:
                if c - dp[m][c] + 1 < length:
                    start = dp[m][c] - 1
                    length = c - dp[m][c] + 1
        
        if length == n + 1:
            return ""
                    
        return S[start:start+length] 
            
