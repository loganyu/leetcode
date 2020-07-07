'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''
# O(n log(sumofarray)) time and O(n) space


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo = max(nums)
        hi = sum(nums)

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            pieces = self.split(nums, mid)
            if pieces > m:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo

    def split(self, nums, largest_sum):
        pieces = 1
        total = 0
        for num in nums:
            total += num
            if total > largest_sum:
                total = num
                pieces += 1

        return pieces

# O(n^2 * m) time and O(n * m) space


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]
        sub = [0] * (n+1)
        for i in range(n):
            sub[i+1] = sub[i] + nums[i]
        f[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j-1], sub[i] - sub[k]))

        return f[n][m]
