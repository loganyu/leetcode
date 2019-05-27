=begin
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
=end

# @param {Integer[][]} intervals
# @return {Boolean}
def can_attend_meetings(intervals)
    intervals.sort_by!{|s,e| s}
    (0...intervals.length-1).each do |i|
        if intervals[i][1] > intervals[i+1][0]
            return false
        end
    end
    
    return true
end
