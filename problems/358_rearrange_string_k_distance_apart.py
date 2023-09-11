'''
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".



Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.


Constraints:

1 <= s.length <= 3 * 105
s consists of only lowercase English letters.
0 <= k <= s.length
'''

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        items = collections.Counter(s).most_common()
        freqs = [f for c, f in items]
        f_max, num_f_max = freqs[0], freqs.count(freqs[0])
        rows = [[] for i in range(f_max)]
        for c, f in items[:num_f_max]:
            for row in rows:
                row.append(c)
        i = 0
        for c, f in items[num_f_max:]:
            while f > 0:
                rows[i].append(c)
                i = (i + 1) % (f_max - 1)
                f -= 1
        ans = []
        for i, row in enumerate(rows):
            if i != f_max - 1 and len(row) < k: return ''
            ans += row
        return ''.join(ans)

