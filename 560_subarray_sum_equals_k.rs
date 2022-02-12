/*
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
*/

use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut k_count = 0;
        let mut sum = 0;
        let mut map: HashMap<i64, i32> = HashMap::new(); 
        map.insert(0, 1);
        for n in nums {
            sum += n as i64; 
            k_count += map.get(&(sum - k as i64)).unwrap_or(&0);
            *map.entry(sum).or_insert(0) += 1;
        }
        k_count
    }
}

