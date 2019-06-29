=begin
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

 

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
=end

# @param {Integer[][]} a
# @return {Integer}
def shortest_bridge(a)
    source, target = get_components(a)
    queue = source.map{|coor| [coor, 0]}
    done = Set.new(source)
    while !queue.empty?
        coor, d = queue.shift
        r, c = coor
        if target.include?([r,c])
            return d-1
        end
        neighbors(r,c,a).each do |nr, nc|
            if !done.include?([nr,nc])
                queue << [[nr,nc],d+1]
                done.add([nr,nc])
            end
        end
    end     
end

def get_components(a)
    done = Set.new
    components = []
    (0...a.length).each do |r|
        (0...a[0].length).each do |c|
            if a[r][c] == 1 && !done.include?([r,c])
                stack = [[r,c]]
                seen = Set.new([[r,c]])
                while !stack.empty?
                    r,c = stack.pop
                    neighbors(r,c,a).each do |nr, nc|
                        if a[nr][nc] == 1 && !seen.include?([nr,nc])
                            stack << [nr,nc]
                            seen.add([nr,nc])
                        end
                    end
                end
                done |= seen
                components << seen
            end
        end
    end

    return components
end

def neighbors(r, c, a)
    neighbors = []
    [[1,0],[-1,0],[0,1],[0,-1]].each do |dr, dc|
        nr = r + dr
        nc = c + dc
        if 0 <= nr && nr < a.length && 0 <= nc && nc < a[0].length
            neighbors << [nr, nc]
        end
    end
    
    return neighbors
end

