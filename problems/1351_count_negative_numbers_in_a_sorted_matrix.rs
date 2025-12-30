/*
 * Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100


Follow up: Could you find an O(n + m) solution?
*/

impl Solution {
    pub fn count_negatives(grid: Vec<Vec<i32>>) -> i32 {
        let mut count = 0;
        let n = grid[0].len();
        let mut curr_row_negative_index = (n - 1) as i32;
        for row in grid {
            while curr_row_negative_index >= 0 && row[curr_row_negative_index as usize] < 0 {
                curr_row_negative_index -= 1;
            }
            count += (n as i32 - (curr_row_negative_index + 1));
        }

        count
    }
}

