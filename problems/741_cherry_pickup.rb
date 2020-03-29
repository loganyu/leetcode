=begin
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

 

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.
 

Your task is to collect maximum number of cherries possible by following the rules below:

 

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
 

 

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
 

Note:

grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
=end

# @param {Integer[][]} grid
# @return {Integer}
def cherry_pickup(grid)
    n = grid.length
    memo = Array.new(n){Array.new(n){Array.new(n)}}
    return [0, dp(0, 0, 0, grid, memo)].max
end

def dp(r1, c1, c2, grid, memo)
    n = grid.length
    r2 = r1 + c1 - c2
    if n == r1 || n == r2 || n == c1 || n == c2 ||
            grid[r1][c1] == -1 || grid[r2][c2] == -1
        return -Float::INFINITY
    elsif r1 == n-1 && c1 == n-1
        return grid[r1][c1]
    elsif !memo[r1][c1][c2].nil?
        return memo[r1][c1][c2]
    else
        ans = grid[r1][c1]
        if c1 != c2
            ans += grid[r2][c2]
        end
        ans += [
            dp(r1, c1+1, c2+1, grid, memo),
            dp(r1+1, c1, c2+1, grid, memo),
            dp(r1, c1+1, c2, grid, memo),
            dp(r1+1, c1, c2, grid, memo)
            ].max
    end
    
    memo[r1][c1][c2] = ans

    return ans
end

