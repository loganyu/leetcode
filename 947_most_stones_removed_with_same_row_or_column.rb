=begin
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
=end

# @param {Integer[][]} stones
# @return {Integer}
def remove_stones(stones)
    graph = Array.new(stones.length){[]}
    (0...stones.length).each do |i|
        (i+1...stones.length).each do |j|
            if stones[i][0] == stones[j][0] || stones[i][1] == stones[j][1]
                graph[i] << j
                graph[j] << i
            end
        end
    end
    
    n = stones.length
    ans = 0
    
    seen = Array.new(n){false}
    
    (0...n).each do |i|
        if !seen[i]
            seen[i] = true
            stack = [i]
            while !stack.empty?
                ans += 1
                node = stack.pop
                graph[node].each do |nei|
                    if !seen[nei]
                        stack << nei
                        seen[nei] = true
                    end
                end
            end
            ans -= 1
        end
    end
    
    return ans
end

