'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
'''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subarrays = 0
        initial_gap = 0
        qsize = 0
        start = 0
        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                qsize += 1
            if qsize == k:
                initial_gap = 0
                while qsize == k:
                    qsize -= nums[start] % 2
                    initial_gap += 1
                    start += 1
            subarrays += initial_gap
        return subarrays

