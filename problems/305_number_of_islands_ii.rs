/*
 * You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:


Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
Example 2:

Input: m = 1, n = 1, positions = [[0,0]]
Output: [1]


Constraints:

1 <= m, n, positions.length <= 104
1 <= m * n <= 104
positions[i].length == 2
0 <= ri < m
0 <= ci < n


Follow up: Could you solve it in time complexity O(k log(mn)), where k == positions.length?
*/

impl Solution {
    pub fn num_islands2(m: i32, n: i32, positions: Vec<Vec<i32>>) -> Vec<i32> {
        let (m, n) = (m as usize, n as usize);
        let mut parent = (0..m*n).into_iter().collect::<Vec<usize>>();
        let mut ret = vec![];
        let mut cnt = 0;
        let mut grid = vec![vec![0; n]; m];
        let dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]];
        for p in positions {
            let (i, j) = (p[0] as usize, p[1] as usize);
            if grid[i][j] == 1 {
                ret.push(cnt);
                continue
            }

            let x = Self::find(&mut parent, i * n + j);

            grid[i][j] = 1;
            cnt += 1;
            for d in dirs {
                let (u, v) = (i as i32 + d[0], j as i32 + d[1]);
                if u < 0 || u == m as i32 || v < 0 || v == n as i32 { continue }

                let (u, v) = (u as usize, v as usize);
                if grid[u][v] == 0 { continue }

                let y = Self::find(&mut parent, u * n + v);
                if y == x { continue }

                cnt -= 1;
                parent[y] = x; // union
            }
            ret.push(cnt);
        }

        ret
    }

    fn find(p: &mut Vec<usize>, i: usize) -> usize {
        if p[i] == i { return i }

        p[i] = Self::find(p, p[i]);
        p[i]
    }
}

