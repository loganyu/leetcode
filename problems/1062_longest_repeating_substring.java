/*
 * Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.



Example 1:

Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.


Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
*/

class Solution {
    public int longestRepeatingSubstring(String s) {
        int length = s.length();
        int[][] dp = new int[length + 1][length + 1];
        int maxLength = 0;
        for (int i = 1; i <= length; i++) {
            for (int j = i + 1; j <= length; j++) {
                if (s.charAt(i - 1) == s.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    maxLength = Math.max(maxLength, dp[i][j]);
                }
            }
        }
        return maxLength;
    }
}

