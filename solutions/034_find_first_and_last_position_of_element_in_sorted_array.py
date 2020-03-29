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
        left_idx = self.extreme_insertion_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
    
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1
        
        return lo
