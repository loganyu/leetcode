/*
 * Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.



Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0


Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
*/

use std::collections::HashSet;
use std::f64;

impl Solution {
    pub fn sum_four_divisors(nums: Vec<i32>) -> i32 {
        let mut sol = 0;
        for &num in &nums {
            let mut divs = HashSet::new();
            let limit = (f64::sqrt(num as f64) + 1.0) as i32;

            for i in 1..limit {
                if num % i == 0 {
                    divs.insert(i);
                    divs.insert(num / i);
                }
                if divs.len() > 4 {
                    break;
                }
            }

            if divs.len() == 4 {
                sol += divs.iter().sum::<i32>();
            }
        }

        sol
    }
}
