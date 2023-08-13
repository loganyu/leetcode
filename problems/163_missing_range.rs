/*
 * You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.





Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.


Constraints:

-109 <= lower <= upper <= 109
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.
*/

impl Solution {
    pub fn find_missing_ranges(nums: Vec<i32>, mut lower: i32, upper: i32) -> Vec<Vec<i32>> {
        if nums.is_empty() {
            return vec![vec![lower, upper]];
        }

        let mut ranges = Vec::new();
        let mut pos = 0;
        while lower < upper && pos < nums.len() {
            if lower < nums[pos] {
                ranges.push(vec![lower, nums[pos] - 1]);
            }
            lower = nums[pos] + 1;
            pos += 1;
        }

        if nums[nums.len() - 1] + 1 <= upper {
            ranges.push(vec![nums[nums.len() - 1] + 1, upper]);
        }
        return ranges;
    }
}

