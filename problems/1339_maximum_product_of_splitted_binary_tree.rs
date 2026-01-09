/*
 * Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)


Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
*/

// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn max_product(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut all_sums = Vec::new();

        fn tree_sum(
            node: Option<Rc<RefCell<TreeNode>>>,
            all_sums: &mut Vec<i64>
        ) -> i64 {
            if let Some(node) = node {
                let node = node.borrow();
                let left_sum = tree_sum(node.left.clone(), all_sums);
                let right_sum = tree_sum(node.right.clone(), all_sums);
                let total_sum = left_sum + right_sum + node.val as i64;
                all_sums.push(total_sum);
                total_sum
            } else {
                0
            }
        }

        let total = tree_sum(root, &mut all_sums);
        let mut best: i64 = 0;

        for &s in &all_sums {
            best = best.max(s * (total - s));
        }

        (best % (1_000_000_007)) as i32
    }
}

