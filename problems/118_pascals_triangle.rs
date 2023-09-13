/*
 * Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
*/

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        let mut cur = vec![vec![1i32]];

        for row in 1..num_rows {
            let mut new_row: Vec<i32> = cur.last().unwrap().windows(2).map(|x| x[0] + x[1]).collect();
            cur.push([&[1], new_row.as_slice(), &[1]].concat());
        }

        cur
    }
}

