'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''
# O(n) time KMP


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        b = [0] * len(needle)
        i, j = 1, 0
        while i < len(needle):
            if needle[i] == needle[j]:
                b[i] = j+1
                i += 1
                j += 1
            elif j > 0:
                j = b[j-1]
            else:
                i += 1

        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = b[j-1]
            else:
                i += 1

        return i - j if j == len(needle) else -1


# O(n^2) time
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        for i in range(n-m+1):
            if haystack[i] == needle[0] and haystack[i:i+m] == needle:
                return i

        return -1
