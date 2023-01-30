/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
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
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut l1 = l1.clone();
        let mut l2 = l2.clone();
        let mut head = Box::new(ListNode::new(0));
        let mut current = &mut head;
      
        let mut carry = 0;
        let mut v1 = 0;
        let mut v2 = 0;
        while l1.is_some() || l2.is_some() || carry != 0 {
            v1 = 0;
            v2 = 0;
            
            if let Some(node) = l1 {
                v1 = node.val;
                l1 = node.next;
            }
            if let Some(node) = l2 {
                v2 = node.val;
                l2 = node.next;
            }
            
            current.next = Some(Box::new(ListNode::new((v1 + v2 + carry) % 10)));
            current = current.next.as_mut().unwrap();
            carry = (v1 + v2 + carry) / 10;
        }
        
        head.next
    }
}

