'''
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
'''
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank, curr, prev):
            visited[curr] = True
            low[curr] = rank
            for neighbor in edges[curr]:
                if neighbor == prev:
                    continue
                if not visited[neighbor]:
                    dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] > rank:
                    self.sol.append([curr, neighbor])
        
        visited = [False]*n
        low = [0]*n
        edges = defaultdict(list)
        self.sol = []
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)
        dfs(0, 0, -1)
        
        return self.sol