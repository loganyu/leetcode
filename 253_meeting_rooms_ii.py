'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        usedRooms = 0
        startTimes = sorted(map(lambda interval: interval[0], intervals))
        endTimes = sorted(map(lambda interval: interval[1], intervals))
        n = len(intervals)
        
        s = e = 0
        while (s < n):
            if startTimes[s] >= endTimes[e]:
                e += 1
            else:
                usedRooms += 1
            s += 1
        
        return usedRooms
        
