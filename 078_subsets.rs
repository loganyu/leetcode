/*
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
*/

impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut subsets: Vec<Vec<i32>> = vec![vec![]];
        let mut tmp;
        for num in nums {
            let mut new_subsets = vec![];
            
            for subset in &subsets {
                tmp = subset.clone();
                tmp.push(num);
                new_subsets.push(tmp);
            }
            subsets.append(& mut new_subsets);
        }
        subsets
    }
}

