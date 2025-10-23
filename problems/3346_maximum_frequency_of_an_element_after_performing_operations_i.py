'''
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.



Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1]. nums becomes [1, 4, 5].
Adding -1 to nums[2]. nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
0 <= k <= 105
0 <= numOperations <= nums.length
'''

import bisect
from collections import Counter

class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)
        candidates = set()
        for num in nums:
            candidates.add(num)
            candidates.add(num - k)
            candidates.add(num + k)
        sorted_nums = sorted(nums)
        max_freq = 0
        for target in candidates:
            already = freq.get(target, 0)
            left = bisect.bisect_left(sorted_nums, target - k)
            right = bisect.bisect_right(sorted_nums, target + k)
            reachable = right - left
            can_modify = reachable - already
            total = already + min(numOperations, can_modify)

            max_freq = max(max_freq, total)

        return max_freq

