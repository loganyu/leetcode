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
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        n = len(intervals)
        s = 0
        e = 0
        rooms = 0
        
        while s < n:
            if start_times[s] >= end_times[e]:
                e += 1
            else:
                rooms += 1
            s += 1
        
        return rooms
                 
