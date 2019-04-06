=begin
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
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
# @return {Interval[]}
def merge(intervals)
    intervals.sort_by!{|interval| interval.start}
    sol = []
    intervals.each do |interval|
        if sol.empty? || sol.last.end < interval.start
            sol << interval
        else
            if sol.last.end < interval.end
                sol.last.end = interval.end
            end
        end
    end
    
    sol
end
