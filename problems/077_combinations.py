'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

# backtracking
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first, curr):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        output = []
        backtrack(1, [])
        return output

# Knuth lexicographic (binary sorted) combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, k+1)) + [n+1]
        output, j = [], 0
        while j < k:
            output.append(nums[:k])
            j = 0
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
        
        return output

