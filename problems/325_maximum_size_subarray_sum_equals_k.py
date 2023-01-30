'''

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
'''

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        longest = 0
        index_by_sum = {0: -1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            if cur_sum - k in index_by_sum:
                longest = max(longest, i - index_by_sum[cur_sum - k])
            if cur_sum not in index_by_sum:
                index_by_sum[cur_sum] = i
        return longest

