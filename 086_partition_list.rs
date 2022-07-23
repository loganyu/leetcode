/*
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
*/

// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn partition(head: Option<Box<ListNode>>, x: i32) -> Option<Box<ListNode>> {
        if head.is_none() {
            return head;
        }
        
        let mut head = head;
        let mut before_head = Box::new(ListNode::new(-1));
        let mut after_head = Box::new(ListNode::new(-1));
        let mut before = &mut before_head;
        let mut after = &mut after_head;
        
        while let Some(mut node) = head {
            if node.val < x {
                head = node.next.take();
                before.next = Some(node);
                before = before.next.as_mut().unwrap();
            } else {
                head = node.next.take();
                after.next = Some(node);
                after = after.next.as_mut().unwrap();
            }
        }
        after.next = None;
        before.next = after_head.next;
        
        before_head.next
    }
}

