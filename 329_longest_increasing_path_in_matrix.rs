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


impl Solution {
    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        let (m, n) = (matrix.len(), matrix[0].len());
        let mut cache = vec![vec![None; n]; m];
        let mut answer = 0;
        for i in 0..m {
            for j in 0..n {
                answer = answer.max(Self::dfs(&matrix, &mut cache, i, j));
            }
        }
        answer
    }
    
    fn dfs(matrix: &[Vec<i32>], cache: &mut Vec<Vec<Option<i32>>>, i: usize, j: usize) -> i32 {
        if let Some(c) = cache[i][j] {
            return c;
        }
        let (m, n) = (matrix.len(), matrix[0].len());
        let mut ret = 1;
        for d in [0, -1, 0, 1, 0].windows(2) {
            let (ni, nj) = (i as i32 + d[0], j as i32 + d[1]);
            if (0..m as i32).contains(&ni) && (0..n as i32).contains(&nj) {
                let (ni, nj) = (ni as usize, nj as usize);
                if matrix[ni][nj] > matrix[i][j] {
                    ret = ret.max(Self::dfs(matrix, cache, ni, nj) + 1);
                }
            }
        }
        cache[i][j] = Some(ret);
        ret
    }
}

