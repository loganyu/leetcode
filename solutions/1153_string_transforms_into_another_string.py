'''
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

 

Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Note:

1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
'''

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        m = {}
        for i in range(len(str1)):
            if str1[i] not in m:
                m[str1[i]] = str2[i]
            elif m[str1[i]] != str2[i]:
                return False
        return len(set(str2)) < 26
        
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        G = {}
        for i in range(len(str1)):
            if str1[i] not in G:
                G[str1[i]] = str2[i]
            elif G[str1[i]] != str2[i]:
                return False
        free = {c for c in string.ascii_lowercase if c not in G}
        for a in list(G.keys()):
            if G[a] == a:
                del G[a]
        while G:
            peel = {a for a, b in G.items() if b not in G}
            if not peel:
                heads = set(G.keys() - set(G.values()))
            if peel:
                free |= peel
                for a in peel:
                    del G[a]
            elif heads:
                a = list(heads)[0]
                seen = collections.defaultdict(list)
                while len(seen[a]) < 2:
                    seen[G[a]].append(a)
                    a = G[a]
                G.pop(seen[a][1])
                free.add(seen[a][1])
            elif free:
                a = list(G.keys())[0]
                G[free.pop()] = G[a]
                G.pop(a)
            else:
                return False
            
        return True
        
