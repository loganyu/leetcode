'''
You are given a string s. You can convert s to a
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.



Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_string = s[::-1]
        combined_string = s + "#" + reversed_string
        prefix_table = self._build_prefix_table(combined_string)
        palindrome_length = prefix_table[-1]
        suffix = reversed_string[: len(s) - palindrome_length]
        return suffix + s

    def _build_prefix_table(self, s: str) -> list:
        prefix_table = [0] * len(s)
        length = 0

        for i in range(1, len(s)):
            while length > 0 and s[i] != s[length]:
                length = prefix_table[length - 1]
            if s[i] == s[length]:
                length += 1
            prefix_table[i] = length
        return prefix_table

