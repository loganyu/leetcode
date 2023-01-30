'''
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        lengths = [1]*n
        counts = [1]*n
        
        for r in range(n):
            for l in range(r):
                if nums[l] < nums[r]:
                    if lengths[l] >= lengths[r]:
                        lengths[r] = 1 + lengths[l]
                        counts[r] = counts[l]
                    elif lengths[l] + 1 == lengths[r]:
                        counts[r] += counts[l]
        
        longest = max(lengths)
        
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest) 
