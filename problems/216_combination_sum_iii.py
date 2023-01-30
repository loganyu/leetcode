'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            
            for i in range(next_start, 10):
                comb.append(i)
                backtrack(remain-i, comb, i+1)
                comb.pop()
            
        backtrack(n, [], 1)
        
        return results
        
