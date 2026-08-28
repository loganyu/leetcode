'''
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.



Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".


Constraints:

1 <= s.length == target.length <= 300
s and target consist of only lowercase English letters.
'''

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        n = len(target)
        res = []

        for i in range(n):
            t = ord(target[i]) - ord("a")

            if cnt[t] > 0:
                cnt[t] -= 1
                if self.can_greater(cnt, target[i + 1 :]):
                    res.append(target[i])
                    continue
                cnt[t] += 1

            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    res.append(chr(c + ord("a")))
                    res.append(
                        "".join(chr(j + ord("a")) * cnt[j] for j in range(26))
                    )
                    return "".join(res)

            return ""

        return ""

    def can_greater(self, cnt: list[int], suffix: str) -> bool:
        max_str = "".join(
            chr(i + ord("a")) * cnt[i] for i in range(25, -1, -1) if cnt[i] > 0
        )
        return max_str > suffix

