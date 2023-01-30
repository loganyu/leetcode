'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    triplets.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
        return list(triplets)
        
