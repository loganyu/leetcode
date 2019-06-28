=begin
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
=end

# @param {Integer[][]} grid
# @return {Integer}
def max_area_of_island(grid)
    max_area = 0
    (0...grid.length).each do |r|
        (0...grid[0].length).each do |c|
            if grid[r][c] == 1
                area = flood_and_get_area(r, c, grid)
                max_area = [max_area, area].max
            end
        end
    end
    
    return max_area
end

def flood_and_get_area(r, c, grid)
    area = 1
    grid[r][c] = 0
    queue = [[r,c]]
    while !queue.empty?
        r, c = queue.shift
        [[1,0],[-1,0],[0,1],[0,-1]].each do |dr, dc|
            nr = r + dr
            nc = c + dc
            if 0 <= nr && nr < grid.length && 0 <= nc && nc < grid[0].length && grid[nr][nc] == 1
                grid[nr][nc] = 0
                area += 1
                queue << [nr, nc]
            end
        end
    end
    
    return area
end

