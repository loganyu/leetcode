'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        self.backtrack(nums, 0, sol)
        
        return sol
        
    def backtrack(self, nums, first, sol):
        if len(nums) == first:
            sol.append(nums[:])
        
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(nums, first+1, sol)
            nums[first], nums[i] = nums[i], nums[first]
 
