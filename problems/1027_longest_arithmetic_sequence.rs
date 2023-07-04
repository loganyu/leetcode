/*
 * Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
Note that:
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
Example 1:
Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
Example 2:
Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].
Example 3:
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].
Constraints:
2 <= nums.length <= 1000
0 <= nums[i] <= 500
*/

use std::collections::HashMap;

impl Solution {
    pub fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
        let mut dp = HashMap::new();
        let n = nums.len();

        for s in 0..n {
            for e in s+1..n {
                let v = *dp.entry((s, nums[e] - nums[s])).or_insert(1);
                dp.insert((e, nums[e] - nums[s]), v + 1);
            }
        }

        *dp.values().max().unwrap()

    }
}

