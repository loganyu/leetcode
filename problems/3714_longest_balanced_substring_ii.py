'''
You are given a string s consisting only of the characters 'a', 'b', and 'c'.

A substring of s is called balanced if all distinct characters in the substring appear the same number of times.

Return the length of the longest balanced substring of s.



Example 1:

Input: s = "abbac"

Output: 4

Explanation:

The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

Example 2:

Input: s = "aabcc"

Output: 3

Explanation:

The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

Example 3:

Input: s = "aba"

Output: 2

Explanation:

One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".



Constraints:

1 <= s.length <= 105
s contains only the characters 'a', 'b', and 'c'.
'''

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        p = [[0, 0, 0]]
        for c in s:
            p.append(p[-1][:])
            p[-1]["abc".index(c)] += 1

        ans = 0
        m = {}
        for i, (a, b, c) in enumerate(p):
            for k in [
                (-1, a - b, a - c),
                (-2, a - b, c),
                (-3, b - c, a),
                (-4, c - a, b),
                (-5, b, c),
                (-6, c, a),
                (-7, a, b),
            ]:
                if not k in m: m[k] = i
                else: ans = max(ans, i - m[k])

        return ans

