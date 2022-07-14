/*
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
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
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut nodes: Vec<Rc<RefCell<TreeNode>>> = match root {
            Some(a) => vec![a],
            None => vec![],
        };
        let mut levels = vec![];
        while nodes.len() > 0 {
            let mut row = vec![];
            let mut next_nodes: Vec<Rc<RefCell<TreeNode>>> = vec![];
            for node in &nodes {
                if let Some(l) = node.borrow().left.clone() {
                    next_nodes.push(l);
                }
                if let Some(r) = node.borrow().right.clone() {
                    next_nodes.push(r);
                }
                row.push(node.borrow().val.clone());
            }
            levels.push(row);
            nodes = next_nodes;
        }

        levels
        
    }
}

