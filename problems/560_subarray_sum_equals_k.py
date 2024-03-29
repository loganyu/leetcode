'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        k_count = 0
        s = 0
        count_by_sum = defaultdict(int)
        count_by_sum[0] = 1
        for num in nums:
            s += num
            if s - k in count_by_sum:
                k_count += count_by_sum[s - k]
            count_by_sum[s] += 1
        
        return k_count

