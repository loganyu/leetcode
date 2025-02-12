'''
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.



Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".


Constraints:

1 <= s.length <= 1000
1 <= part.length <= 1000
s​​​​​​ and part consists of lowercase English letters.
'''

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        kmp_lps = self._compute_longest_prefix_suffix(part)
        char_stack = []
        pattern_indexes = [0] * (len(s) + 1)
        str_index = 0
        pattern_index = 0
        while str_index < len(s):
            current_char = s[str_index]
            char_stack.append(current_char)
            if current_char == part[pattern_index]:
                pattern_indexes[len(char_stack)] = pattern_index + 1
                pattern_index += 1
                if pattern_index == len(part):
                    for _ in range(len(part)):
                        char_stack.pop()
                    pattern_index = (
                        0
                        if not char_stack
                        else pattern_indexes[len(char_stack)]
                    )
            else:
                if pattern_index != 0:
                    str_index -= 1
                    pattern_index = kmp_lps[pattern_index - 1]
                    char_stack.pop()
                else:
                    pattern_indexes[len(char_stack)] = 0

            str_index += 1

        return "".join(char_stack)

    def _compute_longest_prefix_suffix(self, pattern: str) -> list:
        lps = [0] * len(pattern)

        current = 1
        prefix_length = 0
        while current < len(pattern):
            if pattern[current] == pattern[prefix_length]:
                prefix_length += 1
                lps[current] = prefix_length
                current += 1

            elif prefix_length != 0:
                prefix_length = lps[prefix_length - 1]

            else:
                lps[current] = 0
                current += 1

        return lps

