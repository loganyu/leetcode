=begin
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
=end

# @param {Integer[][]} grid
# @return {Integer}
def shortest_distance(grid)
    height = grid.length
    width = grid[0].length
    deltas = [[0,1], [0,-1], [1,0], [-1,0]]
    distance = Array.new(height){Array.new(width){0}}
    reachable_buildings = Array.new(height){Array.new(width){0}}
    buildings = 0
    walkable = 0
    (0...height).each do |row|
        (0...width).each do |col|
            if grid[row][col] != 1
                next
            end
            buildings += 1
            queue = [[row,col]]
            level = 1
            while !queue.empty?
                queue.length.times do
                    curr = queue.shift()
                    deltas.each do |delta|
                        next_row = curr[0] + delta[0]
                        next_col = curr[1] + delta[1]
                        if (next_row >= 0 && next_row < height && 
                            next_col >= 0 && next_col < width &&
                            grid[next_row][next_col] == walkable
                        )
                            grid[next_row][next_col] -= 1
                            distance[next_row][next_col] += level
                            reachable_buildings[next_row][next_col] += 1
                            queue.push([next_row, next_col])
                        end
                    end
                end
                level += 1
            end
            walkable -= 1
        end
    end

    shortest_distance = -1
    (0...height).each do |row|
        (0...width).each do |col|
            if reachable_buildings[row][col] == buildings
                if shortest_distance == -1 || shortest_distance > distance[row][col]
                    shortest_distance = distance[row][col]
                end
            end
        end
    end
    
    return shortest_distance 
end