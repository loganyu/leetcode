/*
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
*/

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        if matrix.len() == 0 {
            return false;
        }

        let m = matrix.len();
        let n = matrix[0].len();
        let mut l = 0;
        let mut r = m * n;

        while l < r {
            let mid = (l + r) / 2;
            let row = mid / n;
            let col = mid % n;

            if target == matrix[row][col] {
                return true;
            } else if target < matrix[row][col] {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        false
    }
}

