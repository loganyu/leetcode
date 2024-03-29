=begin
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
=end

# @param {Integer} n
# @param {Integer[][]} connections
# @return {Integer[][]}
def critical_connections(n, connections)
    @edges = {}
    connections.each do |i,j|
        @edges[i] ||= []
        @edges[i] << j
        @edges[j] ||= []
        @edges[j] << i
    end
    
    @visited = [false]*n
    @low = [0]*n
    @sol = []
    dfs(0, 0, -1)

    return @sol
end

def dfs(rank, curr, prev)
    @visited[curr] = true
    @low[curr] = rank
    @edges[curr].each do |nei|
        if nei == prev
            next
        end
        if !@visited[nei]
            dfs(rank + 1, nei, curr)
        end
        @low[curr] = [@low[curr], @low[nei]].min
        if @low[nei] > rank
            @sol << [nei, curr]
        end
    end
end
