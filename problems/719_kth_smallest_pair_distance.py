'''
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.



Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Example 2:

Input: nums = [1,1,1], k = 2
Output: 0
Example 3:

Input: nums = [1,6,1], k = 3
Output: 5


Constraints:

n == nums.length
2 <= n <= 104
0 <= nums[i] <= 106
1 <= k <= n * (n - 1) / 2
'''

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        array_size = len(nums)
        low = 0
        high = nums[array_size - 1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            count = self._count_pairs_with_max_distance(nums, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    def _count_pairs_with_max_distance(
        self, nums: List[int], max_distance: int
    ) -> int:
        count = 0
        array_size = len(nums)
        left = 0

        for right in range(array_size):
            while nums[right] - nums[left] > max_distance:
                left += 1
            count += right - left
        return count

