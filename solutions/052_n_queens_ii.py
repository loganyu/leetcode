'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        diag1 = set()
        diag2 = set()
        used_cols = set()
        
        
        return self.helper(n, diag1, diag2, used_cols, 0)

    def helper(self, n, diag1, diag2, used_cols, row):
        if row == n:
            return 1
        solutions = 0
        
        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in used_cols:
                continue
            diag1.add(row + col)
            diag2.add(row - col)
            used_cols.add(col)
            
            solutions += self.helper(n, diag1, diag2, used_cols, row + 1)
            
            diag1.remove(row + col)
            diag2.remove(row - col)
            used_cols.remove(col)
        
        return solutions

