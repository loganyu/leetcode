'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.



Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"


Constraints:

1 <= n <= 10
1 <= k <= 100
'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""
        result = ["a"] * n
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c
        for char_index in range(1, n):
            midpoint = 1 << (n - char_index - 1)
            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)

