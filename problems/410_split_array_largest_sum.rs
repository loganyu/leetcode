/*
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

 

Example 1:

Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
Example 2:

Input: nums = [1,2,3,4,5], m = 2
Output: 9
Example 3:

Input: nums = [1,4,4], m = 3
Output: 4
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.length)
*/

impl Solution {
    pub fn split_array(nums: Vec<i32>, m: i32) -> i32 {
        let n = nums.len();
        let mut r = nums.iter().sum::<i32>();
        let mut l = *nums.iter().max().unwrap();
        while l < r {
            let mid = l + (r - l) / 2;
            let mut acc = 0;
            let mut bucket_ct = 1;
            for i in 0..n {
                if acc + nums[i] <= mid {
                    acc += nums[i];
                } else {
                    acc = nums[i];
                    bucket_ct += 1;
                }
            }
            if bucket_ct > m {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        l
    }
}

