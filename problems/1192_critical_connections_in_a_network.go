/*
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
*/

func criticalConnections(n int, connections [][]int) [][]int {
	var dfs func(int, int)
	visited := make(map[int]int)
	var rank int
	graph := make([][]int, n)

	critical := make([][]int, 0)
    dfs = func(v int, p int) {
		visited[v] = rank
		currentRank := rank
		rank++

		for i := 0; i < len(graph[v]); i++ {
			to := graph[v][i]
			if to == p {
				continue
			}

			if _, ok := visited[to]; !ok {
				dfs(to, v)
			}
			visited[v] = min(visited[to], visited[v])
			if currentRank < visited[to] {
				critical = append(critical, []int{v, to})
			}
		}
	}
    
	for _, connection := range connections {
		graph[connection[0]] = append(graph[connection[0]], connection[1])
		graph[connection[1]] = append(graph[connection[1]], connection[0])
	}

	dfs(0, 0)

	return critical
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

