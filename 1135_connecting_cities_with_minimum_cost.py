'''
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
 

Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]
'''

# Prim's Algorithm
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        G = defaultdict(list)
        for city1, city2, cost in connections:
            G[city1].append((cost, city2))
            G[city2].append((cost, city1))
        queue = [(0, N)]
        visited = set()
        total = 0
        while queue and len(visited) < N:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total += cost
                for edge_cost, next_city in G[city]:
                    heapq.heappush(queue, (edge_cost, next_city))
        
        return total if len(visited) == N else -1

# Krushkal's algorithm
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(c1, c2):
            root1, root2 = find(c1), find(c2)
            if root1 == root2:
                return False
            parent[root2] = root1
            return True
        
        parent = {city: city for city in range(1, N+1)}
        connections.sort(key=lambda x: x[2])
        total = 0
        for city1, city2, cost in connections:
            if union(city1, city2):
                total += cost
        root = find(N)

        return total if all(root == find(city) for city in range(1, N+1)) else -1

