/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
*/

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        use std::collections::HashSet;

        let set = nums.into_iter().collect::<HashSet<i32>>();
        let mut longest = 0;
        for num in &set {
            if !set.contains(&(*num - 1)) {
                let mut curr = *num;
                let mut longer = 1;
                while set.contains(&(curr + 1)) {
                    curr += 1;
                    longer += 1;
                }
                longest = std::cmp::max(longest, longer)
            }
        }
        longest
    }
}

