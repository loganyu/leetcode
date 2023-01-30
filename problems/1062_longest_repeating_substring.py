'''
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.



Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 

Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
'''

# Rabin-Karp O(N logN) time and O(N) space


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        a = 26
        modulus = 2**32

        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            if self.search(m, a, modulus, n, nums) != -1:
                l = m + 1
            else:
                r = m - 1

        return l - 1

    def search(self, L, a, modulus, n, nums):
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
        seen = set([h])
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)

        return -1


# O(N^2) time and O(N) space
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        l, r = 1, n
        while l <= r:
            m = l + (r - l) // 2
            if self.search(m, S) != -1:
                l = m + 1
            else:
                r = m - 1

        return l - 1

    def search(self, length, S):
        n = len(S)
        seen = set()
        for s in range(n - length + 1):
            tmp = S[s:s+length]
            if tmp in seen:
                return s
            seen.add(tmp)

        return -1

# O(N^2) time and O(N) space


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        ans = 0
        for i in range(1, len(S)):
            if ans >= len(S)-i:
                break

            tmp = 0
            for x, y in zip(S[i:], S[:-i]):
                if x == y:
                    tmp += 1
                    ans = max(ans, tmp)
                else:
                    tmp = 0

        return ans
