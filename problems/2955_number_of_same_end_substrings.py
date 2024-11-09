'''
You are given a 0-indexed string s, and a 2D array of integers queries, where queries[i] = [li, ri] indicates a substring of s starting from the index li and ending at the index ri (both inclusive), i.e. s[li..ri].

Return an array ans where ans[i] is the number of same-end substrings of queries[i].

A 0-indexed string t of length n is called same-end if it has the same character at both of its ends, i.e., t[0] == t[n - 1].

A substring is a contiguous non-empty sequence of characters within a string.



Example 1:

Input: s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]
Output: [1,5,5,10]
Explanation: Here is the same-end substrings of each query:
1st query: s[0..0] is "a" which has 1 same-end substring: "a".
2nd query: s[1..4] is "bcaa" which has 5 same-end substrings: "bcaa", "bcaa", "bcaa", "bcaa", "bcaa".
3rd query: s[2..5] is "caab" which has 5 same-end substrings: "caab", "caab", "caab", "caab", "caab".
4th query: s[0..5] is "abcaab" which has 10 same-end substrings: "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab", "abcaab".
Example 2:

Input: s = "abcd", queries = [[0,3]]
Output: [4]
Explanation: The only query is s[0..3] which is "abcd". It has 4 same-end substrings: "abcd", "abcd", "abcd", "abcd".


Constraints:

2 <= s.length <= 3 * 104
s consists only of lowercase English letters.
1 <= queries.length <= 3 * 104
queries[i] = [li, ri]
0 <= li <= ri < s.length
'''

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        char_freq_prefix_sum = [[0] * n for _ in range(26)]
        for i, char in enumerate(s):
            char_freq_prefix_sum[ord(char) - ord("a")][i] += 1
        for freq in char_freq_prefix_sum:
            for j in range(1, n):
                freq[j] += freq[j - 1]
        results = []
        for left_index, right_index in queries:
            count_same_end_substrings = 0
            for freq in char_freq_prefix_sum:
                left_freq = 0 if left_index == 0 else freq[left_index - 1]
                right_freq = freq[right_index]
                frequency_in_range = right_freq - left_freq
                count_same_end_substrings += (
                    frequency_in_range * (frequency_in_range + 1) // 2
                )
            results.append(count_same_end_substrings)

        return results

