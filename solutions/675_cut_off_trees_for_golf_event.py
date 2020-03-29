'''
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
 

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Hint: size of the given matrix will not exceed 50x50.
'''

# TLE in LeetCode
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = []
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                if forest[r][c] not in (0,1):
                    trees.append((forest[r][c],r,c))
        trees.sort()
        
        steps = 0
        
        sr = 0
        sc = 0
        for tree in trees:
            _, er, ec = tree
            distance = self.distance(sr, sc, er, ec, forest)
            if distance == -1:
                return -1
            steps += distance
            sr = er
            sc = ec
        
        return steps
    
    def distance(self, sr, sc, er, ec, forest):
        queue = deque([(sr,sc,0)])
        visited = set([(sr,sc)])
        while queue:
            r,c,d = queue.popleft()
            if r == er and c == ec:
                return d
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < len(forest) and 
                    0 <= nc < len(forest[0]) and 
                    (nr,nc) not in visited and
                    forest[nr][nc] != 0):
                    queue.append((nr,nc,d+1))
                    visited.add((nr,nc))
        
        return -1
        
