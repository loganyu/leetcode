'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = low = high = nums[0]
        for num in nums[1:]:
            high, low = max(high*num, low*num,
                            num), min(high*num, low*num, num)
            max_prod = max(max_prod, high)

        return max_prod
