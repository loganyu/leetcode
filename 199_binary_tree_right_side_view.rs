/*
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let node = match root {
            Some(a) => a,
            None => return vec![],
        };
        
        let mut res = vec![];
        let mut queue = VecDeque::new();
        queue.push_back(node);
        
        while queue.len() > 0 {
            let end = queue.len() - 1;
            res.push( queue[end].borrow().val.clone() );
            
            for _ in 0..=end {
                let node = queue.pop_front().unwrap();
                if let Some(ref left) = node.clone().borrow().left {
                    queue.push_back(left.clone());
                }
                if let Some(ref right) = node.clone().borrow().right {
                    queue.push_back(right.clone());
                }
            }
        }
        
        res
        
    }
}

