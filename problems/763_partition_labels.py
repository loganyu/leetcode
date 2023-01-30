'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = {}
        for i, char in enumerate(S):
            last_idx[char] = i
        
        s = 0
        e = 0
        parts = []
        for i, char in enumerate(S):
            if last_idx[char] > e:
                e = last_idx[char]
            if i == e:
                parts.append(e-s+1)
                s = e+1

        return parts
