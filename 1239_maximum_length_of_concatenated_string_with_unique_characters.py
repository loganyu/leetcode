'''
Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.backtracking(arr, 0, Counter())
    
    def backtracking(self, arr: List[str], pos: int, res_map: Counter[str]) -> int:
        if len(res_map) and res_map.most_common(1)[0][1] > 1:
            return 0
        best = len(res_map)
        
        for i in range(pos, len(arr)):
            word_map = Counter(arr[i])
            if len(word_map) != len(arr[i]):
                continue
            res_map.update(word_map)
            best = max(best, self.backtracking(arr, i+1, res_map))
            
            for c in word_map:
                if res_map[c] == word_map[c]:
                    del res_map[c]
                else:
                    res_map[c] -= word_map[c]
        
        return best
        
