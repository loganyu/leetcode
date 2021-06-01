'''
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

 

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.
 


 

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

 

Example:

Input: m = 1, n = 1
Output: 9
'''

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        res = 0
        used = [False] * 9
        for length in range(m, n+1):
            res += self.calc_patterns(-1, length, used)
        return res
    
    def calc_patterns(self, last, length, used):
        if length == 0:
            return 1
        total = 0
        for i in range(9):
            if self.is_valid(i, last, used):
                used[i] = True
                total += self.calc_patterns(i, length-1, used)
                used[i] = False
        
        return total
    
    def is_valid(self, i, last, used):
        if used[i]:
            return False
        if last == -1:
            return True
        if (i+last) % 2 == 1:
            return True
        
        mid = (i+last)//2
        if mid == 4:
            return used[mid]
        if (i%3 != last%3) and (i//3 != last//3):
            return True
        return used[mid]
        
