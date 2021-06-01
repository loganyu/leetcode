'''
Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:

k will be a positive integer.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them.
 

Example 1:

Input: s = "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.
Example 2:

Input: s = "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
Example 3:

Input: s = "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
Example 4:

Input: s = "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
Example 5:

Input: s = "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
 

Constraints:

1 <= s.length <= 150
s consists of only lowercase English letters.
'''

class Solution:
    def encode(self, s: str) -> str:
        n = len(s)
        dp = [[None for _ in range(n)] for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                j = i+l
                substr = s[i:j+1]
                if j - i < 4:
                    dp[i][j] = substr
                else:
                    dp[i][j] = substr
                    for k in range(i, j):
                        if len(dp[i][k] + dp[k+1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k+1][j]
                    
                    for k in range(len(substr)):
                        repeat_str = substr[0:k+1]
                        if repeat_str and len(substr) % len(repeat_str) == 0 and len(substr.replace(repeat_str, "")) == 0:
                            ss = str(len(substr) // len(repeat_str)) + "[" + dp[i][i+k] + "]"
                            if len(ss) < len(dp[i][j]):
                                dp[i][j] = ss
        for r in dp: print(r)
        
        return dp[0][n-1]

