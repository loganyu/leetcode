=begin
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
=end

# @param {Character[][]} grid
# @return {Integer}
# bfs
def num_islands(grid)
    if (grid.nil? || grid.empty?)
        return 0
    end
    
    nr = grid.length
    nc = grid[0].length
    num_islands = 0
    0.upto(nr-1).each do |r|
        0.upto(nc-1).each do |c|
            if grid[r][c] == '1'
                num_islands += 1
                grid[r][c] == '0'
                neighbors = []
                neighbors.push([r,c])
                while (!neighbors.empty?)
                    rc = neighbors.pop
                    row = rc[0]
                    col = rc[1]
                    if (row-1 >= 0 && grid[row-1][col] == '1')
                        neighbors.push([row-1,col])
                        grid[row-1][col] = '0'
                    end
                    if (row+1 < nr && grid[row+1][col] == '1')
                        neighbors.push([row+1,col])
                        grid[row+1][col] = '0'
                    end
                    if (col-1 >= 0 && grid[row][col-1] == '1')
                        neighbors.push([row,col-1])
                        grid[row][col-1] = '0'
                    end
                    if (col+1 < nc && grid[row][col+1] == '1')
                        neighbors.push([row,col+1])
                        grid[row][col+1] = '0'
                    end
                end
            end     
        end
    end
    
    return num_islands
end

# dfs
def num_islands(grid)
    if (grid.nil? || grid.empty?)
        return 0
    end
    
    nr = grid.length
    nc = grid[0].length
    num_islands = 0
    grid.each_with_index do |row, r|
        row.each_with_index do |val, c|
            if val == '1'
                num_islands += 1
                dfs(grid, r, c, nr, nc)
            end
        end
    end
    
    return num_islands
end

def dfs(grid, r, c, nr, nc)
    if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0')
        return
    end
    
    grid[r][c] = '0'
    dfs(grid, r - 1, c, nr, nc)
    dfs(grid, r + 1, c, nr, nc)
    dfs(grid, r, c - 1, nr, nc)
    dfs(grid, r, c + 1, nr, nc)
end