/*
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
*/

func maxAreaOfIsland(grid [][]int) int {
    max := 0
    h, w := len(grid), len(grid[0])
    visited := make([][]int, h)
    for i := range visited {
        visited[i] = make([]int, w)
    }
    
    for i, row := range grid {
        for j := range row {
            area := getArea(i, j, grid, visited, h, w)
            if area > max {
                max = area
            }
        }
    }
    return max
}

func getArea(i int, j int, grid [][]int, visited [][]int, h int, w int) int {
    if i < 0 || i >= h || j < 0 || j >= w || grid[i][j] != 1 || visited[i][j] == 1 {
        return 0
    }
    area := 1
    visited[i][j] = 1
    area += getArea(i-1, j, grid, visited, h, w)
    area += getArea(i+1, j, grid, visited, h, w)
    area += getArea(i, j-1, grid, visited, h, w)
    area += getArea(i, j+1, grid, visited, h, w)
    
    return area
}

