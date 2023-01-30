/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
*/

func generate(numRows int) [][]int {
    arr := make([][]int,numRows)
    for i := 0; i < numRows; i++{
        arr[i] = make([]int,i+1)
    }
    for i := 0; i < numRows; i++ {
        for j := 0; j < len(arr[i]); j++ {
            if (j == 0 || j == len(arr[i]) - 1) {
                arr[i][j] = 1
            }else{
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            }
        }
    }
    return arr
}

