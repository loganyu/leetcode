/*
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
*/

class Solution {
    private int[][] grid;
    private boolean[][] seen;
    private Set<Pair<Integer, Integer>> shape;
    private int rowOrigin;
    private int colOrigin;
    private void explore(int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length)
            return;
        if (grid[row][col] == 0 || seen[row][col])
            return;
        seen[row][col] = true;
        shape.add(new Pair<>(row - rowOrigin, col - colOrigin));
        explore(row+1, col);
        explore(row-1, col);
        explore(row, col+1);
        explore(row, col-1);
    }
    
    public int numDistinctIslands(int[][] grid) {
        this.grid = grid;
        this.seen = new boolean[grid.length][grid[0].length];
        Set<Set<Pair<Integer, Integer>>> shapes = new HashSet<>();
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                this.shape = new HashSet<>();
                this.rowOrigin = row;
                this.colOrigin = col;
                explore(row, col);
                if (!shape.isEmpty())
                    shapes.add(shape);
            }
        }

        return shapes.size();
    }
}

