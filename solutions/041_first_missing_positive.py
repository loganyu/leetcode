'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        if n == 1:
            return 2
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        
        for i in range(n):
            a = abs(nums[i])
            if a == n:
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])
        
        for i in range(1, n):
            if nums[i] > 0:
                return i
        
        if nums[0] > 0:
            return n
        
        return n + 1
    
