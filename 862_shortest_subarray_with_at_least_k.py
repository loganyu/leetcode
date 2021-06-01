'''
Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

 

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
 

Note:

1 <= A.length <= 50000
-10 ^ 5 <= A[i] <= 10 ^ 5
1 <= K <= 10 ^ 9
'''

from collections import deque

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        prefix = [0]
        for num in A:
            prefix.append(prefix[-1] + num)
        ans = n+1
        monoq = deque()
        for i, total in enumerate(prefix):
            while monoq and total <= prefix[monoq[-1]]:
                monoq.pop()
                
            while monoq and total - prefix[monoq[0]] >= K:
                ans = min(ans, i - monoq.popleft())
            
            monoq.append(i)
        
        return ans if ans < n+1 else -1
        
