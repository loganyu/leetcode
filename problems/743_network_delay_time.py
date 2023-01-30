'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''

# Dijkstra's heap O(E logE) time and O(N + E) space
from collections import defaultdict
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w,v))
        
        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            
            for d2, nei in graph[node]:
                if nei not in dist:
                    heappush(pq, (d+d2, nei))
        
        return max(dist.values()) if len(dist) else -1

# Dijkstra's basic O(N**2 + E) and O(N + E) space
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w,v))
        
        dist = {node: float('inf') for node in range(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0
        
        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i
            
            if cand_node < 0:
                break
            seen[cand_node] = True
            for d, nei in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)
        
        ans = max(dist.values())
        
        return ans if ans < float('inf') else -1

# dfs O(N**N + ElogE) time and O(N + E) space
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w,v))
        
        dist = {node: float('inf') for node in range(1, N+1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)
        
        dfs(K, 0)
        ans = max(dist.values())
        
        return ans if ans < float('inf') else -1
    
