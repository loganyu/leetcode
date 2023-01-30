'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        for r in range(min(k, n)):
            min_heap.append((matrix[r][0], r, 0))
        heapq.heapify(min_heap)
        
        while k:
            element, r, c = heapq.heappop(min_heap)
            if c < n - 1:
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
            k -= 1
        
        return element
        
