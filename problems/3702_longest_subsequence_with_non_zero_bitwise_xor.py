'''
You are given an integer array nums.

Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.



Example 1:

Input: nums = [1,2,3]

Output: 2

Explanation:

One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.

Example 2:

Input: nums = [2,3,4]

Output: 3

Explanation:

The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.



Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
'''

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        totalXor = 0
        allZero = True

        for x in nums:
            totalXor ^= x
            if x > 0:
                allZero = False

        if totalXor > 0:
            return n
        return n - 1 if allZero == False else 0

