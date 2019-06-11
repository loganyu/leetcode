'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sol = [1]*n
        left = 1
        for i in range(1,n):
            left *= nums[i-1]
            sol[i] *= left
            
        right = 1
        for j in range(n-2,-1,-1):
            right *= nums[j+1]
            sol[j] *= right
        
        return sol

