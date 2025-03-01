'''
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.



Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)
        dp = [
            [0 for _ in range(str2_length + 1)] for _ in range(str1_length + 1)
        ]
        for row in range(str1_length + 1):
            dp[row][0] = row
        for col in range(str2_length + 1):
            dp[0][col] = col
        for row in range(1, str1_length + 1):
            for col in range(1, str2_length + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1
        super_sequence = []
        row, col = str1_length, str2_length
        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                super_sequence.append(str1[row - 1])
                row -= 1
            else:
                super_sequence.append(str2[col - 1])
                col -= 1
        while row > 0:
            super_sequence.append(str1[row - 1])
            row -= 1
        while col > 0:
            super_sequence.append(str2[col - 1])
            col -= 1
            
        return "".join(super_sequence[::-1])
        
        
