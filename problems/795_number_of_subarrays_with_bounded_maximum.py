'''
We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
Input: 
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

left, right, and nums[i] will be an integer in the range [0, 109].
The length of nums will be in the range of [1, 50000].
'''

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, dp = 0, 0
        prev = -1
        for i, num in enumerate(nums):
            if num < left and i > 0:
                ans += dp
            elif num > right:
                dp = 0
                prev = i
            elif left <= num <= right:
                dp = i - prev
                ans += dp
                
        return ans
            
