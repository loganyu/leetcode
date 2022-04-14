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

impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>> {
        let n = n as usize;
        let mut ret = vec![vec![0; n]; n];

        let mut num = 1;
        for i in 0..((n + 1) / 2) {
            for c in i..(n - 1 - i) {
                ret[i][c] = num;
                num += 1;
            }
            for r in i..(n - 1 - i) {
                ret[r][n - 1 - i] = num;
                num += 1;
            }
            for c in ((i + 1)..(n - i)).rev() {
                ret[n - 1 - i][c] = num;
                num += 1;
            }
            for r in ((i + 1)..(n - i)).rev() {
                ret[r][i] = num;
                num += 1;
            }
        }
        ret[n / 2][(n - 1) / 2] = (n * n) as i32;

        ret
    }
}

