/*
 * Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.



Example 1:

Input: nums = [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.
Example 2:

Input: nums = [9,9,8,8]
Output: -1
Explanation: There is no number that occurs only once.


Constraints:

1 <= nums.length <= 2000
0 <= nums[i] <= 1000
*/

use std::collections::HashMap;

impl Solution {
    pub fn largest_unique_number(nums: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();
        for num in nums {
            *counts.entry(num).or_insert(0) += 1;
        }

        counts
            .iter()
            .filter(|&(_, &count)| count == 1)
            .map(|(&num, _)| num)
            .max()
            .unwrap_or(-1)
    }
}

