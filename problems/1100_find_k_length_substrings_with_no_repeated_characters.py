'''
Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.



Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
1 <= k <= 104
'''

from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26:
            return 0
        answer = 0
        n = len(s)
        left = right = 0
        freq = Counter()

        while right < n:
            freq[s[right]] += 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1

            if right - left + 1 == k:
                answer += 1
                freq[s[left]] -= 1
                left += 1

            right += 1

        return answer

