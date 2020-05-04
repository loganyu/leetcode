'''
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 

Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        w = []
        sum_ = 0
        for i, num in enumerate(nums):
            sum_ += num
            if i >= k: 
                sum_ -= nums[i-k]
            if i >= k-1:
                w.append(sum_)
        
        left = [0] * len(w)
        best = 0
        for i in range(len(w)):
            if w[i] > w[best]:
                best = i
            left[i] = best
        
        right = [0] * len(w)
        best = len(w) - 1
        for i in reversed(range(len(w))):
            if w[i] >= w[best]:
                best = i
            right[i] = best
            
        ans = None
        for m in range(k, len(w) - k):
            l, r = left[m-k], right[m+k]
            if not ans or (w[l] + w[m] + w[r] > w[ans[0]] + w[ans[1]] + w[ans[2]]):
                ans = l, m, r
        
        return ans

