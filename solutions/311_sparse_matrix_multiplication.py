'''
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(B[0])
        sol = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for r in range(rows):
            for i in range(cols):
                if A[r][i] != 0:
                    for c in range(cols):
                        sol[r][c] += A[r][i] * B[i][c]
        
        return sol
        
