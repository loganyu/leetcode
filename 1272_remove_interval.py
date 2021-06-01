'''
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
'''

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        output = []
        
        for start, end in intervals:
            if end <= remove_start or start >= remove_end:
                output.append([start, end])
            elif start < remove_start and end > remove_end:
                output.append([start, remove_start])
                output.append([remove_end, end])
            elif start < remove_start and end <= remove_end:
                output.append([start, remove_start])
            elif start >= remove_start and end > remove_end:
                output.append([remove_end, end])
        
        return output
    
