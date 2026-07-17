'''
You are given an integer array nums and an integer target.

Return the number of subarrays of nums in which target is the majority element.

The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.



Example 1:

Input: nums = [1,2,2,3], target = 2

Output: 5

Explanation:

Valid subarrays with target = 2 as the majority element:

nums[1..1] = [2]
nums[2..2] = [2]
nums[1..2] = [2,2]
nums[0..2] = [1,2,2]
nums[1..3] = [2,2,3]
So there are 5 such subarrays.

Example 2:

Input: nums = [1,1,1,1], target = 1

Output: 10

Explanation:

​​​​​​​All 10 subarrays have 1 as the majority element.

Example 3:

Input: nums = [1,2,3], target = 4

Output: 0

Explanation:

target = 4 does not appear in nums at all. Therefore, there cannot be any subarray where 4 is the majority element. Hence the answer is 0.



Constraints:

1 <= nums.length <= 10​​​​​​​5
1 <= nums[i] <= 10​​​​​​​9
1 <= target <= 109
'''

from collections import Counter

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        prefix_counts = Counter({0: 1})
        current_sum = 0
        total_valid_subarrays = 0
        smaller_counts = 0
        for num in nums:
            if num == target:
                smaller_counts += prefix_counts[current_sum]
                current_sum += 1
            else:
                current_sum -= 1
                smaller_counts -= prefix_counts[current_sum]
            total_valid_subarrays += smaller_counts

            prefix_counts[current_sum] += 1

        return total_valid_subarrays

