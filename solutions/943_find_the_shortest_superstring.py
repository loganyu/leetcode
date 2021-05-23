'''
Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.

 

Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
 

Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlaps = [[0] * n for _ in range(n)]
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i != j:
                    for ans in reversed(range(min(len(x), len(y)))):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break
        dp = [[0] * n for _ in range(1<<n)]
        parent = [[None] * n for _ in range(1<<n)]
        for mask in range(1, 1<<n):
            for bit in range(n):
                if (mask >> bit) & 1:
                    pmask = mask ^ (1 << bit)
                    if pmask == 0:
                        continue
                    for i in range(n):
                        if (pmask >> i) & 1:
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i
                                
                                
        perm = []
        mask = (1<<n) - 1
        i = max(range(n), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]
        
        perm = perm[::-1]
        seen = [False] * n
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(n) if not seen[i]])
        
        ans = [words[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(words[perm[i]][overlap:])
        
        return "".join(ans)
                                     
