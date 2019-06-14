=begin
You are given a set of non-overlapping intervals and a requestInterval. Find all non-overlapping intervals.

Example 1:

Input: intervals = [[10,15], [25,35]], requestInterval = [17,27]
Output: [[17,25]]
Example 2:

Input: intervals = [[10,15], [25,35], [45,65], [85,95]], requestInterval = [17,100]
Output: [[17,25], [35,45], [65,85], [95,100]]
=end

def non_overlapping_intervals(intervals, request_interval)
  intervals.sort!
  sol = [request_interval]
  intervals.each do |interval|
    # create two missing intervals b/c interval in inside
    # req: [     ]
    # int:   [ ]
    # new: [ ] [ ]
    if interval[0] > sol.last[0] && interval[1] < sol.last[1]
      new_interval = [interval[-1], sol.last[-1]]
      sol.last[-1] = interval[0]
      sol.push(new_interval)
    # no missing interval since interval is greater
    # req:     [ ]
    # int:   [     ]
    # new:   none
    elsif interval[0] <= sol.last[0] && interval[1] >= sol.last[1]
      return []
    # replace end of request interval
    # req: [   ]
    # int:   [   ] 
    # new: [ ]
    elsif interval[0] > sol.last[0] && interval[0] < sol.last[1]
      sol.last[1] = interval[0]
    # replace beginning of request interval
    # req:   [   ]
    # int: [   ] 
    # new:     [ ]
    elsif interval[1] > sol.last[0] && interval[1] < sol.last[1]
      sol.last[0] = interval[1]
    end
  end

  return sol
end

# intervals = [[10,15], [25,35]]
# request_interval = [17,27]

# intervals = [[10,15], [25,35], [45,65], [85,95]]
# request_interval = [17,100]

intervals = [[0,4],[15,101]]
request_interval = [17,100]

puts non_overlapping_intervals(intervals, request_interval).inspect
