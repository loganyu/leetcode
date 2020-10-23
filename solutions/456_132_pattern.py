'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 104
-109 <= nums[i] <= 109
'''

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        mins = [None] * n
        mins[0] = nums[0]
        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])
        for j in reversed(range(n)):
            while stack and stack[-1] <= mins[j]:
                stack.pop()
            if stack and stack[-1] < nums[j]:
                return True
            stack.push(nums[j])
        
        return False
        
