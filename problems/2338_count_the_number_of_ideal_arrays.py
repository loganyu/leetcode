'''
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays):
   - With no other distinct values (1 array): [1,1,1,1,1]
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.


Constraints:

2 <= n <= 104
1 <= maxValue <= 104
'''

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        m = min(n, 14)
        dp = [[0] * (m+1) for _ in range(maxValue+1)]
        for i in range(1, maxValue+1):
            dp[i][1] = 1
            j = 2
            while i * j <= maxValue:
                for k in range(1, m):
                    dp[i*j][k+1] += dp[i][k]
                j += 1
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i-1] * i % mod
        invfact = [1] * n
        invfact[n-1] = pow(fact[n-1], mod-2, mod)
        for i in range(n-1, 0, -1):
            invfact[i-1] = invfact[i] * i % mod
        res = 0
        f_n1 = fact[n-1]
        for i in range(1, maxValue+1):
            for k in range(1, m+1):
                res = (res + dp[i][k] * f_n1 % mod * invfact[k-1] % mod * invfact[n-k] % mod) % mod
        return res

