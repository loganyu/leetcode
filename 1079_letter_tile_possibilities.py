'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''

# counting
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = [0] * 26
        for char in tiles:
            count[ord(char) - ord('A')] += 1
        
        def dfs():
            total = 0
            for i in range(26):
                if count[i] == 0:
                    continue
                total += 1
                count[i] -= 1
                total += dfs()
                count[i] += 1
                
            return total
        
        return dfs()
        
# keeping track of sequence
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        def dfs(path, t):
            if path in res:
                return
            if path:
                res.add(path)
            for i in range(len(t)):
                dfs(path+t[i], t[:i] + t[i+1:])
        dfs('', tiles)
        
        return len(res)
