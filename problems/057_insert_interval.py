'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        n = len(intervals)
        i = 0
        while i < n and newInterval[0] > intervals[i][0]:
            output.append(intervals[i])
            i += 1
        
        if not output or output[-1][1] < newInterval[0]:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newInterval[1])
            
        while i < n:
            interval = intervals[i]
            start, end = interval
            if output[-1][1] < start:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], end)
            i += 1
        
        return output
                   
