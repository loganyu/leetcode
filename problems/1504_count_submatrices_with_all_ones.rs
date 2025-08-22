/*
 * Given an m x n binary matrix mat, return the number of submatrices that have all ones.



Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2.
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3.
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2.
There are 2 rectangles of side 3x1.
There is 1 rectangle of side 3x2.
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.


Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.
*/

use std::cmp;

impl Solution {
    pub fn num_submat(mut mat: Vec<Vec<i32>>) -> i32 {
        if mat.is_empty() || mat[0].is_empty() {
            return 0;
        }
        let rows = mat.len();
        let cols = mat[0].len();
        for r in 0..rows {
            for c in 1..cols {
                if mat[r][c] == 1 {
                    mat[r][c] += mat[r][c - 1];
                }
            }
        }
        let mut submatrices = 0;
        for r in 0..rows {
            for c in 0..cols {
                if mat[r][c] > 0 {
                    let mut min_width = mat[r][c];
                    for current_row in r..rows {
                        if mat[current_row][c] == 0 {
                            break;
                        }
                        min_width = cmp::min(min_width, mat[current_row][c]);
                        submatrices += min_width;
                    }
                }
            }
        }
        
        submatrices
    }
}
