/*
 * Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
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
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::step(&root)
    }
    fn step(node: &Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match node {
            Some(node) => {
                let node = node.borrow();
                match &node.left {
                    Some(left) => {
                        let left = left.borrow();

                        if left.left.is_none() && left.right.is_none() {
                            left.val + Self::step(&node.right)
                        } else {
                            Self::step(&node.left) + Self::step(&node.right)
                        }
                    }
                    None => Self::step(&node.right),
                }
            }
            None => 0,
        }
    }
}

