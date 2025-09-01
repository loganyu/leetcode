/*
 * Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.



Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
*/

impl Solution {
    pub fn find_diagonal_order(mat: Vec<Vec<i32>>) -> Vec<i32> {
        if mat.is_empty() {
            return vec![];
        }

        let n = mat.len();
        let m = mat[0].len();
        let total_elements = n * m;

        let mut result = Vec::with_capacity(total_elements);

        let mut row: i32 = 0;
        let mut col: i32 = 0;

        let mut direction: i32 = 1;

        for _ in 0..total_elements {
            result.push(mat[row as usize][col as usize]);
            row -= direction;
            col += direction;
            if row >= n as i32 {
                row = (n - 1) as i32;
                col += 2;
                direction *= -1;
            }
            else if col >= m as i32 {
                col = (m - 1) as i32;
                row += 2;
                direction *= -1;
            }
            else if row < 0 {
                row = 0;
                direction *= -1;
            }
            else if col < 0 {
                col = 0;
                direction *= -1;
            }
        }

        result

    }
}
