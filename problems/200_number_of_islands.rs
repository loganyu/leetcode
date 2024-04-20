/*
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
*/

use std::collections::VecDeque;

impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let (m, n) = (grid.len(), grid[0].len());
        let mut q = VecDeque::with_capacity(m * n);
        let mut n_islands = 0;
        for i in 0..m {
            for j in 0..n {
                if grid[i][j] == '1' {
                    n_islands += 1;
                    q.push_back((i, j));
                    while !q.is_empty() {
                        for _ in 0..q.len() {
                            let (k, l) = q.pop_front().unwrap();
                            if k < m && l < n && grid[k][l] == '1' {
                                grid[k][l] = '0';
                                for w in [0, 1, 0, !0, 0].windows(2) {
                                    q.push_back((k.wrapping_add(w[0]), l.wrapping_add(w[1])));
                                }
                            }
                        }
                    }
                }
            }
        }
        n_islands
    }
}

