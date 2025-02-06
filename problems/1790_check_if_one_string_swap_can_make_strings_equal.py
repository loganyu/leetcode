'''
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.



Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.


Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
'''

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_frequency_map = [0] * 26
        s2_frequency_map = [0] * 26
        num_diffs = 0

        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]

            if s1_char != s2_char:
                num_diffs += 1
                if num_diffs > 2:
                    return False

            s1_frequency_map[ord(s1_char) - ord("a")] += 1
            s2_frequency_map[ord(s2_char) - ord("a")] += 1

        return s1_frequency_map == s2_frequency_map

