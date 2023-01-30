/*
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
*/

func longestIncreasingPath(matrix [][]int) int {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return 0
    }
    row, col := len(matrix), len(matrix[0])
    cache := make([][]int, row)
    for i:= range cache {
        cache[i] = make([]int, col)
    }
    result := 0
    for i := 0; i < row; i++{
        for j := 0; j < col; j++{
            result = max(result, helper(matrix, i, j, cache))
        }
    }
    return result
}

func helper(matrix [][]int, i, j int, cache [][]int) int{
    if cache[i][j] != 0{
        return cache[i][j]
    }
    
    dx:= []int{-1,1,0,0}
    dy:= []int{0,0,1,-1}
    
    for k := 0; k < 4; k++ {
        x := i + dx[k]
        y := j + dy[k]
        
        if x >= 0 && y >= 0 && x < len(matrix) && y <len(matrix[0]) && matrix[x][y] > matrix[i][j] {
            cache[i][j]= max(cache[i][j],helper(matrix, x, y, cache))
        }
    }
    cache[i][j] = 1 + cache[i][j]
    return cache[i][j]
}

func max(a,b int) int{
    if a > b {
        return a
    }
    return b
}

