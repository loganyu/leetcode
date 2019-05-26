=begin
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
=end

# @param {Integer[][]} grid
# @return {Integer}
def num_distinct_islands(grid)
    shapes = Set.new
    (0...grid.length).each do |r|
        (0...grid[0].length).each do |c|
            shape = Set.new
            explore(r, c, r, c, grid, shape)
            if !shape.empty?
                shapes.add(shape)
            end
        end
    end
    
    return shapes.count
end

def explore(r, c, ro, co, grid, shape)
    if r.between?(0, grid.length-1) && c.between?(0, grid[0].length-1) && grid[r][c] == 1
        grid[r][c] = 0
        shape.add([r - ro, c - co])
        explore(r+1, c, ro, co, grid, shape)
        explore(r-1, c, ro, co, grid, shape)
        explore(r, c+1, ro, co, grid, shape)
        explore(r, c-1, ro, co, grid, shape)
    end
end

