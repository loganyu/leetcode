2419_longest_subarray_with_maximum_bitwise_AND.rs/*
 * You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.



Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
*/

use std::cmp::max;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        if nums.is_empty() {
            return 0;
        }

        let mut max_val = nums[0];
        let mut ans = 0;
        let mut current_streak = 0;

        for &num in &nums {
            if num > max_val {
                max_val = num;
                current_streak = 1;
            } else if num == max_val {
                current_streak += 1;
            } else {
                current_streak = 0;
            }
            ans = max(ans, current_streak);
        }
        ans
    }
}

