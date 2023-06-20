/*
 * Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
*/

impl Solution {
    pub fn min_meeting_rooms(intervals: Vec<Vec<i32>>) -> i32 {
        let mut start = vec![];
        let mut end = vec![];
        for i in intervals {
            start.push(i[0]);
            end.push(i[1]);
        }
        start.sort();
        end.sort();
        let mut s = 0;
        let mut e = 0;
        let mut used_rooms = 0;
        while s < start.len() {
            if start[s] >= end[e] {
                e += 1;
            } else {
                used_rooms += 1;
            }
            s += 1;
        }
        used_rooms
    }
}

