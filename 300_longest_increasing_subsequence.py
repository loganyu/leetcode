'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [None]*n
        dp[0] = 1
        max_ans = 1
        for e in range(n):
            max_val = 0
            for s in range(e):
                if nums[s] < nums[e]:
                    max_val = max(max_val, dp[s])
            dp[e] = max_val + 1
            max_ans = max(max_ans, dp[e])
        
        return max_ans
            
