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

impl Solution {
    pub fn total_n_queens(n: i32) -> i32 {
        if n < 1 { return 0; }

        let mut result = 0;
        let mut cols = vec![];
        let mut xy_sum = vec![];
        let mut xy_sub = vec![];
        let row = 0;

        Self::_dfs(n, &mut result, row, &mut cols, &mut xy_sum, &mut xy_sub);

        result
    }

    pub fn _dfs(n: i32, result: &mut i32, row: i32, cols: &mut Vec<i32>, xy_sum: &mut Vec<i32>, xy_sub: &mut Vec<i32>) {
        if row >= n {
            *result += 1;
            return;
        }

        for col in 0..n {
            if cols.contains(&col) || xy_sum.contains(&(row + col)) || xy_sub.contains(&(row - col)) {
                continue;
            }

            cols.push(col);
            xy_sum.push(row + col);
            xy_sub.push(row - col);
            Self::_dfs(n, result, row + 1, cols, xy_sum, xy_sub);

            cols.retain(|&x| x != col);
            xy_sum.retain(|&x| x != (row + col));
            xy_sub.retain(|&x| x != (row - col));
        }
    }
}

