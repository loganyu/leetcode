'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
'''

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {i: [] for i in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        components = 0
        for i in range(n):
            queue = [i]
            components += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]
                    
        return components
        
