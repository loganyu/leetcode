/*
 * There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.



Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.


Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
*/

class Solution {
    public int strangePrinter(String s) {
        s = removeDuplicates(s);
        int n = s.length();
        int[][] minTurns = new int[n][n];
        for (int i = 0; i < n; i++) {
            minTurns[i][i] = 1;
        }
        for (int length = 2; length <= n; length++) {
            for (int start = 0; start + length - 1 < n; start++) {
                int end = start + length - 1;
                minTurns[start][end] = length;
                for (int split = 0; split < length - 1; split++) {
                    int totalTurns =
                        minTurns[start][start + split] +
                        minTurns[start + split + 1][end];
                    if (s.charAt(start + split) == s.charAt(end)) {
                        totalTurns--;
                    }
                    minTurns[start][end] = Math.min(
                        minTurns[start][end],
                        totalTurns
                    );
                }
            }
        }
        return minTurns[0][n - 1];
    }

    private String removeDuplicates(String s) {
        StringBuilder uniqueChars = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            char currentChar = s.charAt(i);
            uniqueChars.append(currentChar);
            while (i < s.length() && s.charAt(i) == currentChar) {
                i++;
            }
        }
        return uniqueChars.toString();
    }
}

