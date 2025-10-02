'''
Given an integer array nums sorted in non-decreasing order and an integer k, return true if this array can be divided into one or more disjoint increasing subsequences of length at least k, or false otherwise.



Example 1:

Input: nums = [1,2,2,3,3,4,4], k = 3
Output: true
Explanation: The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
Example 2:

Input: nums = [5,6,6,7,8], k = 3
Output: false
Explanation: There is no way to divide the array using the conditions required.


Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
nums is sorted in non-decreasing order.
'''

class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        pre = nums[0]
        cnt = 0
        for n in nums:
            if pre == n:
                cnt += 1
            else:
                pre = n
                cnt = 1
            if cnt * k > len(nums):
                return False
        return True

