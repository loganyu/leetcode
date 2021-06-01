'''
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

Note:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
'''

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.sol = []
        self.nums = nums
        self.backtrack(0, [])
        
        return self.sol
    
    def backtrack(self, s, path):
        if s == len(self.nums):
            return
        seen = set()
        for i in range(s, len(self.nums)):
            if self.nums[i] in seen:
                continue
            if path and path[-1] > self.nums[i]:
                continue
            seen.add(self.nums[i])
            path.append(self.nums[i])
            if len(path) >= 2:
                self.sol.append(path[:])
            self.backtrack(i+1, path)
            path.pop()
        
