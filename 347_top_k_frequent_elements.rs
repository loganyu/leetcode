/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*/

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        use std::collections::{HashMap, BinaryHeap};
         
        let mut res = Vec::with_capacity(k as usize);
        let mut occurence_map = HashMap::new();
        for num in &nums {
            *occurence_map.entry(num).or_insert(0) += 1;
        }
        let mut heap = BinaryHeap::new();
        for (num, o) in occurence_map {
             heap.push((o, num));
        }
        
        for _ in 0..k {
            let (_, num) = heap.pop().unwrap();
            res.push(*num);
        }
        
        res
    }
}
