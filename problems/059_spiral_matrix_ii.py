'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        matrix = [[None for _ in range(n)] for _ in range(n)]
        limit = n**2
        r = c = 0
        val = 1
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        
        while val <= limit:
            matrix[r][c] = val
            r += dirs[d][0]
            c += dirs[d][1]
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c]:
                r -= dirs[d][0]
                c -= dirs[d][1]
                d = (d+1) % 4
                r += dirs[d][0]
                c += dirs[d][1]
            val += 1
        
        return matrix
            
