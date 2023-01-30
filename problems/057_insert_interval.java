/*
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
*/

class Solution {
    boolean doesIntervalsOverlap(int[] a, int[] b) {
        return Math.min(a[1], b[1]) - Math.max(a[0], b[0]) >= 0;
    }

    int[] mergeIntervals(int[] a, int[] b) {
        int[] newInterval = {Math.min(a[0], b[0]), Math.max(a[1], b[1])};
        return newInterval;
    }

    int UpperBound(int[][] intervals, int[] newInterval) {
        if (intervals.length == 0) {
            return 0;
        }

        int start = 0, end = intervals.length - 1;
        int ans = intervals.length;
        while (start <= end) {
            int mid = (start + end) / 2;
            if (intervals[mid][0] > newInterval[0]) {
                ans = mid;
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return ans;
    }

    int[][] insertInterval(int[][] intervals, int[] newInterval) {
        List<int[]> list = new ArrayList<>(Arrays.asList(intervals));
        int index = UpperBound(intervals, newInterval);

        if (index != intervals.length) {
            list.add(index, newInterval);
        } else {
            list.add(newInterval);
        }

        return list.toArray(new int[list.size()][2]);
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        intervals = insertInterval(intervals, newInterval);
        List<int[]> answer = new ArrayList<>();
        for (int i = 0; i < intervals.length; i++) {
            int[] currInterval = {intervals[i][0], intervals[i][1]};
            // Merge until the list gets exhausted or no overlap is found.
            while (i < intervals.length && doesIntervalsOverlap(currInterval, intervals[i])) {
                currInterval = mergeIntervals(currInterval, intervals[i]);
                i++;
            }
            i--;
            answer.add(currInterval);
        }

        return answer.toArray(new int[answer.size()][2]);
    }
}

