/*
 * Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
*/

impl Solution {
    pub fn triangle_number(nums: Vec<i32>) -> i32 {
        if nums.len() < 3 {
            return 0;
        }
        let mut sorted_nums = nums;
        sorted_nums.sort_unstable();

        let n = sorted_nums.len();
        let mut count = 0;

        for k in (2..n).rev() {
            let c = sorted_nums[k];

            let mut left = 0;
            let mut right = k - 1;

            while left < right {
                let a = sorted_nums[left];
                let b = sorted_nums[right];

                if a + b > c {
                    count += (right - left) as i32;
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }

        count
    }
}

