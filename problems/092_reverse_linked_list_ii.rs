/*
 * Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
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
    pub fn reverse_between(head: Option<Box<ListNode>>, left: i32, right: i32) -> Option<Box<ListNode>> {
        let mut dummy = Some(Box::new(ListNode {
            val: 0,
            next: head,
        }));
        let mut before = &mut dummy;
        for _ in 1..left {
            before = &mut before.as_mut()?.next;
        }

        let mut node = before.as_mut()?.next.take();
        let mut node2 = node.as_mut()?.next.take();
        for _ in left..right {
            let node3 = node2.as_mut()?.next.take();
            node2.as_mut()?.next = node;
            node = node2;
            node2 = node3;
        }

        let mut rev_tail = &mut node;
        for _ in left..right {
            rev_tail = &mut rev_tail.as_mut()?.next;
        }
        rev_tail.as_mut()?.next = node2;
        before.as_mut()?.next = node;

        dummy.unwrap().next
    }
}

