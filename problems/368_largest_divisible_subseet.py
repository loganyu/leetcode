'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
'''

# O(N^2) time and O(N^2) space
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
            
        return list(max(subsets.values(), key=len))
        

