'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''

# O(N) time and O(N) space
from heapq import heappush, heappop
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque()
        mind = deque()
        l = 0
        res = 0
        for r, num in enumerate(nums):
            while maxd and num > maxd[-1]:
                maxd.pop()
            while mind and num < mind[-1]:
                mind.pop()
            maxd.append(num)
            mind.append(num)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[l]:
                    maxd.popleft()
                if mind[0] == nums[l]:
                    mind.popleft()
                l += 1
            res = max(res, r - l + 1)

        return res


# O(N log N) time and O(N) space


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxq, minq = [], []
        res = i = 0
        for j, num in enumerate(nums):
            heappush(maxq, [-num, j])
            heappush(minq, [num, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heappop(maxq)
                while minq[0][1] < i:
                    heappop(minq)
            res = max(res, j - i + 1)

        return res
