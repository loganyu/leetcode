'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        count = 1
        upper = math.sqrt(n)
        passed = [False]*n
        for i in range(3, n, 2):
            if passed[i]:
                continue
            count += 1
            if i > upper:
                continue
            j = i*i
            while j < n:
                passed[j] = True
                j += 2*i
        
        return count

