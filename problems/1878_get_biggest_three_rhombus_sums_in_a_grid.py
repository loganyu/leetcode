'''
You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 105
'''

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        heap = []

        def update_heap(num):
            if num in heap:
                return
            if len(heap) < 3:
                heappush(heap, num)
            elif heap[0] < num:
                heapreplace(heap, num)

        def explore(row, col, dist):
            if dist == 0:
                num = grid[row][col]
                update_heap(num)
                explore(row, col, dist + 1)
                return
            up = row + dist
            down = row - dist
            left = col - dist
            right = col + dist

            if up >= m or down < 0 or right >= n or left < 0:
                return
            num = grid[up][col] + grid[down][col] + grid[row][left] + grid[row][right]
            u, d, r, l = up - 1, down + 1, col + 1, col - 1
            while u > row:
                num += grid[u][r] + grid[u][l] + grid[d][l] + grid[d][r]
                u -= 1
                d += 1
                l -= 1
                r += 1
            update_heap(num)
            explore(row, col, dist + 1)

        for row in range(m):
            for col in range(n):
                explore(row, col, 0)

        return sorted(heap, reverse=True) 

