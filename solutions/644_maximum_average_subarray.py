'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is greater than or equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation:
- When the length is 4, averages are [0.5, 12.75, 10.5] and the maximum average is 12.75
- When the length is 5, averages are [10.4, 10.8] and the maximum average is 10.8
- When the length is 6, averages are [9.16667] and the maximum average is 9.16667
The maximum average is when we choose a subarray of length 4 (i.e., the sub array [12, -5, -6, 50]) which has the max average 12.75, so we return 12.75
Note that we do not consider the subarrays of length < 4.
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 104
-104 <= nums[i] <= 104
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        hi = max(nums)
        lo = min(nums)
        
        precision = 1E-6
        while hi - lo > precision:
            mid = (hi + lo) / 2
            if self.can_process(nums, mid, k):
                lo = mid
            else:
                hi = mid
        return lo
    
    def can_process(self, nums, mid, k):
        sum_so_far = min_so_far = prev = 0.0
        for i in range(k):
            sum_so_far += nums[i] - mid
        if sum_so_far >= 0:
            return True
        for i in range(k, len(nums)):
            sum_so_far += nums[i] - mid
            prev += nums[i-k] - mid
            min_so_far = min(min_so_far, prev)
            if sum_so_far >= min_so_far:
                return True
        return False
        
