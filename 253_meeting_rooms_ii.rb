=begin
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
=end

# Definition for an interval.
# class Interval
#     attr_accessor :start, :end
#     def initialize(s=0, e=0)
#         @start = s
#         @end = e
#     end
# end

# @param {Interval[]} intervals
# @return {Integer}
def min_meeting_rooms(intervals)
    if intervals.empty?
        return 0
    end
    
    used_rooms = 0
    start_timings = intervals.map(&:start).sort
    end_timings = intervals.map(&:end).sort
    l = intervals.length
    
    end_pointer = 0
    start_pointer = 0
    
    while start_pointer < l
        if start_timings[start_pointer] >= end_timings[end_pointer]
            end_pointer += 1
        else
            used_rooms += 1
        end
        start_pointer += 1
    end
    
    return used_rooms
end