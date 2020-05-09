'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
'''

# memoization
# O(l) space and 0(n) time
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {0: 1}
        for num in nums:
            m = defaultdict(int)
            for sum_, count in memo.items():
                m[sum_ + num] += count
                m[sum_ - num] += count
            memo = m
            
        return memo[S]

# recursion with memoization
# O(l*n) space and O(n) time
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.count = 0
        self.memo = {}
        self.nums = nums
        self.S = S
        
        return self.calculate(0, 0)
    
    def calculate(self, i, total):
        if i == len(self.nums):
            return 1 if total == self.S else 0
        if (i, total) in self.memo:
            return self.memo[(i, total)]
        
        add = self.calculate(i+1, total + self.nums[i])
        subtract = self.calculate(i+1, total - self.nums[i])
        self.memo[(i, total)] = add + subtract
        
        return self.memo[(i, total)]
        

