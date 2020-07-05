'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        
        distances = set()
        for point1, point2 in itertools.combinations((p1, p2, p3, p4), 2):
            distances.add(distance(point1, point2))
        
        return 0 not in distances and len(distances) == 2
        
