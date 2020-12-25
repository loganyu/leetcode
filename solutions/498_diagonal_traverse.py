'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
'''

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        r = c = 0
        d = 1
        sol = []
        
        for _ in range(n*m):
            sol.append(matrix[r][c])
            r -= d
            c += d
            if r >= n:
                r -= 1
                c += 2
                d *= -1
            elif c < 0:
                c += 1
                d *= -1
            elif c >= m:
                c -= 1
                r += 2
                d *= -1
            elif r < 0:
                r += 1
                d *= -1


        return sol
        
