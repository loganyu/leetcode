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

# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    sol = []
    intervals.sort_by{|s,e| s}.each do |interval|
        if sol.empty? || sol.last[1] < interval[0]
            sol << interval
        elsif sol.last[1] < interval[1]
            sol.last[1] = interval[1]
        end
    end
    
    return sol
end