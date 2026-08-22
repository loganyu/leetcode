'''
You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.



Example 1:

Input: coins = [3,6,9], k = 3

Output: 9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:

Input: coins = [5,2], k = 7

Output: 12

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.



Constraints:

1 <= coins.length <= 15
1 <= coins[i] <= 25
1 <= k <= 2 * 109
coins contains pairwise distinct integers.
'''

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        n = len(coins)
        m = 1 << n
        left = k
        right = coins[0] * k + 1

        bit_count = [0] * m
        lcm = [0] * m

        for mask in range(1, m):
            cur_lcm = 1

            for i, coin in enumerate(coins):
                if mask >> i & 1:
                    cur_lcm = cur_lcm // gcd(cur_lcm, coin) * coin
                    bit_count[mask] += 1

            lcm[mask] = cur_lcm

        def count(x: int) -> int:
            res = 0

            for mask in range(1, m):
                if lcm[mask] <= x:
                    if bit_count[mask] & 1:
                        res += x // lcm[mask]
                    else:
                        res -= x // lcm[mask]

            return res

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left

