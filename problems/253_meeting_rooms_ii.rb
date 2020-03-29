=begin
iven an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
=end

# @param {Integer[][]} intervals
# @return {Integer}
def min_meeting_rooms(intervals)
    if intervals.empty?
        return 0
    end
    
    used_rooms = 0
    start_timings = intervals.map{|s,e| s}.sort
    end_timings = intervals.map{|s,e| e}.sort
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