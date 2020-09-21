'''
There is a strange printer with the following two special requirements:

On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
Once the printer has used a color for the above operation, the same color cannot be used again.
You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.

Return true if it is possible to print the matrix targetGrid, otherwise, return false.

 

Example 1:



Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
Output: true
Example 2:



Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
Output: true
Example 3:

Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
Output: false
Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.
Example 4:

Input: targetGrid = [[1,1,1],[3,1,3]]
Output: false
 

Constraints:

m == targetGrid.length
n == targetGrid[i].length
1 <= m, n <= 60
1 <= targetGrid[row][col] <= 60
'''

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        dep = [set() for _ in range(61)]
        n = len(targetGrid)
        m = len(targetGrid[0])
        for i in range(1, 61):
            min_r = n
            min_c = m
            max_r = -1
            max_c = -1
            for r in range(n):
                for c in range(m):
                    if targetGrid[r][c] == i:
                        min_r = min(min_r, r)
                        min_c = min(min_c, c)
                        max_r = max(max_r, r)
                        max_c = max(max_c, c)
            
            for tr in range(min_r, max_r + 1):
                for tc in range(min_c, max_c + 1):
                    if targetGrid[tr][tc] != i:
                        dep[i].add(targetGrid[tr][tc])
            
        def has_cycle(i):
            visited[i] = 1
            for d in dep[i]:
                if visited[d] == 2:
                    continue
                if visited[d] == 1:
                    return True
                if has_cycle(d):
                    return True
            visited[i] = 2

            return False

        visited = [0 for _ in range(61)]
        for i in range(1, 61):
            if visited[i] == 0 and has_cycle(i):
                return False

        return True
        
