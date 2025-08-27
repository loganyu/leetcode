'''
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        longest_window = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            longest_window = max(longest_window, i - start)

        return longest_window

