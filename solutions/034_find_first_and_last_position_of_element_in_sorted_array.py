'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_left_index(nums, target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        right = self.find_right_index(nums, target)
        
        return [left, right]
    
    def find_left_index(self, nums, target):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
                
        return lo
    
    def find_right_index(self, nums, target):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
        
        return lo - 1
