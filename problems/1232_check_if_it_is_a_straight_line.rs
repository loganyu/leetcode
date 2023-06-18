/*
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
*/

impl Solution {
    pub fn check_straight_line(coordinates: Vec<Vec<i32>>) -> bool {
        if coordinates.len() == 2 {
            return true;
        }
        coordinates.windows(3).all(|points| {
            let (p2, p1, p0) = (&points[2], &points[1], &points[0]);
            (p2[1] - p1[1]) * (p1[0] - p0[0]) ==  (p1[1] - p0[1]) * (p2[0] - p1[0])
        })
    }
}

