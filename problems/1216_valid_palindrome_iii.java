/*
 * Given a string s and an integer k, return true if s is a k-palindrome.

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
*/

class Solution {
    public boolean isValidPalindrome(String s, int k) {
        int memo[] = new int[s.length()];
        int temp, prev;
        for (int i = s.length() - 2; i >= 0; i--) {
            prev = 0;
            for (int j = i + 1; j < s.length(); j++) {
                temp = memo[j];
                if (s.charAt(i) == s.charAt(j))
                    memo[j] = prev;
                else
                    memo[j] = 1 + Math.min(memo[j], memo[j - 1]);
                prev = temp;
            }
        }
        return memo[s.length() - 1] <= k;
    }
}

