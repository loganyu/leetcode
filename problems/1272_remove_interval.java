/*
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
*/

class Solution {
    public List<List<Integer>> removeInterval(int[][] intervals, int[] toBeRemoved) {
        int removeStart = toBeRemoved[0], removeEnd = toBeRemoved[1];
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        
        for (int[] interval : intervals) {
            int start = interval[0], end = interval[1];
            if (end <= removeStart || start >= removeEnd) {
                output.add(new ArrayList<Integer>() {{add(start); add(end); }});
                
            } else if (start < removeStart && end > removeEnd) {
                output.add(new ArrayList<Integer>() {{add(start); add(removeStart); }});
                output.add(new ArrayList<Integer>() {{add(removeEnd); add(end); }});
                    
            } else if (start < removeStart && end <= removeEnd) {
                output.add(new ArrayList<Integer>() {{add(start); add(removeStart); }});
            } else if (start >= removeStart && end > removeEnd) {
                output.add(new ArrayList<Integer>() {{add(removeEnd); add(end); }});
            }
        }
        
        return output;
    }
}

