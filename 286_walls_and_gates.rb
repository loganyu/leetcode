=begin
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
=end

# @param {Integer[][]} rooms
# @return {Void} Do not return anything, modify rooms in-place instead.
def walls_and_gates(rooms)
    queue = []
    (0...rooms.length).each do |r|
        (0...rooms[0].length).each do |c|
            if rooms[r][c] == 0
                queue << [r,c]
            end
        end
    end
    
    while !queue.empty?
        r, c = queue.shift
        [[1,0],[-1,0],[0,1],[0,-1]].each do |dr, dc|
            nr = r + dr
            nc = c + dc
            if 0 <= nr && nr < rooms.length && 0 <= nc && nc < rooms[0].length &&
                rooms[nr][nc] == 2**31-1
                rooms[nr][nc] = rooms[r][c] + 1
                queue << [nr,nc]
            end
        end
    end
end

