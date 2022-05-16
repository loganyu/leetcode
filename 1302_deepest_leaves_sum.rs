/*
Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
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
use std::collections::VecDeque;

impl Solution {
    pub fn deepest_leaves_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut vd = VecDeque::new();
        if let Some(r) = root {
            vd.push_back(r);
        }
        let mut answer = 0;
        while !vd.is_empty() {
            answer = 0;
            for _ in 0..vd.len() {
                if let Some(n) = vd.pop_front() {
                    answer += n.borrow().val;
                    if let Some(l) = n.borrow_mut().left.take() {
                        vd.push_back(l);
                    }
                    if let Some(r) = n.borrow_mut().right.take() {
                        vd.push_back(r);
                    }
                }
            }
        }
        answer
        
    }
}

