/*
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
*/

func generateMatrix(n int) [][]int {
    matrix := make([][]int, n)
    for i := range matrix {
        matrix[i] = make([]int, n)
    }

    if n == 0 {
        return matrix
    }

    rowStart := 0
    rowEnd := n - 1
    colStart := 0
    colEnd := n - 1
    num := 1

    for rowStart <= rowEnd && colStart <= colEnd {
        for i := colStart; i <= colEnd; i++ {
            matrix[rowStart][i] = num
            num++
        }
        rowStart++

        for i := rowStart;i<=rowEnd; i++ {
            matrix[i][colEnd] = num
            num++
        }
        colEnd--
        for  i:= colEnd; i >= colStart; i-- {
            if rowStart <= rowEnd {
                matrix[rowEnd][i] = num
                num++
            }
        }
        rowEnd--
        for  i:= rowEnd; i >= rowStart; i-- {
            if colStart <= colEnd {
                matrix[i][colStart] = num
                num++
            }
        }
        colStart++
    }
    return matrix
}

