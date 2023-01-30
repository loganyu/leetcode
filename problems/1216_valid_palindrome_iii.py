'''
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true
 

Constraints:

1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length
'''

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)] 
        for i in range(n + 1): 
            for j in range(n + 1): 
                if not i or not j: 
                    dp[i][j] = i or j 
                elif s[i - 1] == s[n - j]: 
                    dp[i][j] = dp[i - 1][j - 1] 
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n] <= k * 2

