/*
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
*/

func minimumEffortPath(heights [][]int) int {
	w, h := len(heights[0]), len(heights)

	dp := make([][]int, h)
	for i := range dp {
		dp[i] = make([]int, w)
		for j := range dp[i] {
			dp[i][j] = math.MaxInt32
		}
	}
	dp[0][0] = 0
	queue := [][]int{{0, 0, 0}}

	for len(queue) > 0 {
		q := queue[0]
		queue = queue[1:]

		for _, d := range dir {
			x, y := q[0]+d[0], q[1]+d[1]

			if validPoint(heights, x, y) {
				if cost := max(q[2], abs(heights[y][x]-heights[q[1]][q[0]])); dp[y][x] > cost {
					dp[y][x] = cost
					queue = append(queue, []int{x, y, cost})
				}
			}
		}
	}

	return dp[h-1][w-1]
}

var dir = [][]int{
	{0, 1},
	{0, -1},
	{1, 0},
	{-1, 0},
}

func validPoint(heights [][]int, x, y int) bool {
	return x >= 0 && y >= 0 && x < len(heights[0]) && y < len(heights)
}

func max(i, j int) int {
	if i >= j {
		return i
	}
	return j
}

func min(i, j int) int {
	if i <= j {
		return i
	}
	return j
}

func abs(i int) int {
	if i >= 0 {
		return i
	}
	return -i
}

