/*
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
*/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        elements = []
        r = c = 0
        dirs_r = [0, 1, 0, -1]
        dirs_c = [1, 0, -1, 0]
        di = 0
        seen = set()
        rows = len(matrix)
        cols = len(matrix[0])
        
        for _ in range(rows * cols):
            elements.append(matrix[r][c])
            seen.add((r,c))
            cr = r + dirs_r[di]
            cc = c + dirs_c[di]
            if 0 <= cr < rows and 0 <= cc < cols and (cr,cc) not in seen:
                r = cr
                c = cc
            else:
                di = (di+1)%4
                r += dirs_r[di]
                c += dirs_c[di]
        
        return elements
