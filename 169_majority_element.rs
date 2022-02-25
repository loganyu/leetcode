/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
*/


impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut count = 1;
        let mut candidate = nums[0];
        for &n in &nums[1..] {
            if count == 0 {
                candidate = n;
            }
            if n == candidate {
                count += 1;
            } else {
                count -= 1;
            }
        }
        candidate
    }
}

