/*
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
*/

impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut sum = 0;
        let mut ret = usize::MAX;

        for (i, &n) in nums.iter().enumerate() {
            sum += n;
            if sum >= target {
                while sum >= target {
                    sum -= nums[l];
                    l += 1;
                }
                ret = ret.min(i - l + 2);
            }
        }
        
        if ret == usize::MAX {
            0
        } else {
            ret as i32
        }
    }
}

