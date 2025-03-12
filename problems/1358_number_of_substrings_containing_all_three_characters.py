'''
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.



Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
Example 3:

Input: s = "abc"
Output: 1


Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = total = 0
        freq = [0] * 3

        while right < len(s):
            freq[ord(s[right]) - ord("a")] += 1

            while self._has_all_chars(freq):
                total += len(s) - right
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

            right += 1

        return total

    def _has_all_chars(self, freq: list) -> bool:
        return all(f > 0 for f in freq)

