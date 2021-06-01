'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''
# O(n*m) time and O(m) space
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [float('inf') for _ in range(cols+1)] 
        dp[cols - 1] = 1
        
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                min_health = min(dp[c], dp[c+1]) - dungeon[r][c]
                if min_health <= 0:
                    min_health = 1
                dp[c] = min_health
        
        return dp[0]

# O(n*m) time and O(n*m) space
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        
        def get_min_health(currCell, nr, nc):
            if nr >= rows or nc >= cols:
                return float('inf')
            nextCell = dp[nr][nc]
            
            return max(1, nextCell - currCell)
        
        for r in reversed(range(rows)):
            for c in reversed(range(cols)):
                currCell = dungeon[r][c]
                
                right_health = get_min_health(currCell, r, c+1)
                down_health = get_min_health(currCell, r+1, c)
                next_health = min(right_health, down_health)
                
                if next_health != float('inf'):
                    min_health = next_health
                else:
                    min_health = 1 if currCell >= 0 else (1 - currCell)
                
                dp[r][c] = min_health
        
        return dp[0][0]
        
        
