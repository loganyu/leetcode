'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index_by_count = {0: -1}
        count = 0
        longest = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in index_by_count:
                longest = max(longest, i - index_by_count[count])
            else:
                index_by_count[count] = i
        
        return longest

