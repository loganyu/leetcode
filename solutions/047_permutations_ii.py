'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        self.backtrack(0, sol, nums)
        
        return list(sol)
    
    def backtrack(self, start, sol, nums):
        if start == len(nums):
            sol.add(tuple(nums[:]))
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.backtrack(start + 1, sol, nums)
            nums[start], nums[i] = nums[i], nums[start]
        
