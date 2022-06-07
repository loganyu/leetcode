/*
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
*/

func totalNQueens(n int) int {
    var result int
    col := make([]bool, n)
    diag1 := make([]bool, n << 1 - 1)
    diag2 := make([]bool, n << 1 - 1)
    
    helper(n, 0, col, diag1, diag2, &result)
    
    return result
}

func helper(n int,
    row int, col []bool, diag1 []bool, diag2[]bool, result *int) {
    if row >= n {
        *result = *result + 1
        return
    }
    
    for i := 0; i < n; i++ {
        if col[i] || diag1[row + i] || diag2[row - i + n - 1] {
            continue
        }
        
        col[i] = true
        diag1[row + i] = true
        diag2[row - i + n - 1] = true
        helper(n, row + 1, col, diag1, diag2, result)
        col[i] = false
        diag1[row + i] = false
        diag2[row - i + n - 1] = false
    }  
}

