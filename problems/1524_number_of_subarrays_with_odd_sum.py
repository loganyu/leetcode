'''
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
'''

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1e9 + 7
        n = len(arr)

        for i in range(n):
            arr[i] %= 2

        dp_even, dp_odd = [0] * n, [0] * n

        if arr[n - 1] == 0:
            dp_even[n - 1] = 1
        else:
            dp_odd[n - 1] = 1

        for num in range(n - 2, -1, -1):
            if arr[num] == 1:
                dp_odd[num] = (1 + dp_even[num + 1]) % MOD
                dp_even[num] = dp_odd[num + 1]
            else:
                dp_even[num] = (1 + dp_even[num + 1]) % MOD
                dp_odd[num] = dp_odd[num + 1]

        count = 0
        for odd_count in dp_odd:
            count += odd_count
            count %= MOD

        return int(count)

