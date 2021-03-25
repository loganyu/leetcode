/*
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
*/

class Solution {
    private static final int[][] DIRS = new int[][]{{0,1}, {1,0}, {-1,0}, {0,-1}};
    private int numRows;
    private int numCols;
    private int[][] landHeights;
    
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0)
            return new ArrayList<>();
        numRows = matrix.length;
        numCols = matrix[0].length;
        landHeights = matrix;
        
        Queue<int[]> pacificQueue = new LinkedList<>();
        Queue<int[]> atlanticQueue = new LinkedList<>();
        
        for (int r = 0; r < numRows; r++) {
            pacificQueue.offer(new int[]{r, 0});
            atlanticQueue.offer(new int[]{r, numCols - 1});
        }
        for (int c = 0; c < numCols; c++) {
            pacificQueue.offer(new int[]{0, c});
            atlanticQueue.offer(new int[]{numRows - 1, c});
        }
        
        boolean[][] pacificReachable = bfs(pacificQueue);
        boolean[][] atlanticReachable = bfs(atlanticQueue);
        
        List<List<Integer>> commonCells = new ArrayList<>();
        for (int r = 0; r < numRows; r++) {
            for (int c = 0; c < numCols; c++) {
                if (pacificReachable[r][c] && atlanticReachable[r][c]) {
                    commonCells.add(List.of(r, c));
                }
            }
        }
        
        return commonCells;
    }
    
    private boolean[][] bfs(Queue<int[]> queue) {
        boolean[][] reachable = new boolean[numRows][numCols];
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            reachable[cell[0]][cell[1]] = true;
            for (int[] dir : DIRS) {
                int newRow = cell[0] + dir[0];
                int newCol = cell[1] + dir[1];
                    
                if (newRow < 0 || newRow >= numRows || newCol < 0 || newCol >= numCols)
                    continue;
                if (reachable[newRow][newCol])
                    continue;
                if (landHeights[newRow][newCol] < landHeights[cell[0]][cell[1]])
                    continue;
                queue.offer(new int[]{newRow, newCol});
            }
        }
        
        return reachable;
    }
}

