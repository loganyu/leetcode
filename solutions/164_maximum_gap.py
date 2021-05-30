'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 109
'''

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lo = min(nums)
        hi = max(nums)
        n = len(nums)
        if n <= 2 or hi == lo:
            return hi - lo
        B = defaultdict(list)
        for num in nums:
            i = n - 2 if num == hi else (num - lo) * (n - 1) // (hi - lo)
            B[i].append(num)
        candidates = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        
        return max(y[0] - x[1] for x, y in zip(candidates, candidates[1:]))
        
