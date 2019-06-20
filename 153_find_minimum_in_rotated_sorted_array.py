'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        
        if nums[r] >= nums[0]:
            return nums[0]
        
        while r >= l:
            m = l + (r-l)//2
            if nums[m] > nums[m+1]:
                return nums[m+1]
            if nums[m-1] > nums[m]:
                return nums[m]
            if nums[m] > nums[0]:
                l = m+1
            else:
                r = m-1
                
