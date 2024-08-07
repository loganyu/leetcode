'''
Given two integer arrays nums1 and nums2 of length n, count the pairs of indices (i, j) such that i < j and nums1[i] + nums1[j] > nums2[i] + nums2[j].

Return the number of pairs satisfying the condition.



Example 1:

Input: nums1 = [2,1,2,1], nums2 = [1,2,1,2]
Output: 1
Explanation: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 > 1 + 1.
Example 2:

Input: nums1 = [1,10,6,2], nums2 = [1,4,1,5]
Output: 5
Explanation: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 > 1 + 4.
- (0, 2) where 1 + 6 > 1 + 1.
- (1, 2) where 10 + 6 > 4 + 1.
- (1, 3) where 10 + 2 > 4 + 5.
- (2, 3) where 6 + 2 > 1 + 5.


Constraints:

n == nums1.length == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 105
'''

class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        difference = [nums1[i] - nums2[i] for i in range(N)]
        difference.sort()
        result = 0
        left = 0
        right = N - 1
        while left < right:
            if difference[left] + difference[right] > 0:
                result += right - left
                right -= 1
            else:
                left += 1
        return result

