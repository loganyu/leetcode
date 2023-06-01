/*
 * In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.



Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.
Example 2:


Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7.
Example 3:


Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.


Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105
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
    pub fn pair_sum(mut head: Option<Box<ListNode>>) -> i32 {
        let mut slow = &head;
        let mut fast = &head;
        while fast.is_some() {
            slow = &slow.as_ref().unwrap().next;
            fast = &fast.as_ref().unwrap().next.as_ref().unwrap().next;
        }
        let mut prev: Option<Box<ListNode>> = None;
        let mut cur = slow.clone();
        while let Some(mut node) = cur.take() {
            let next = node.next.take();
            node.next = prev.take();
            prev = Some(node);
            cur = next;
        }
        let mut back = prev;
        let mut max_sum = i32::MIN;
        while let Some(mut b_node) = back.take() {
            let mut f_node = head.unwrap();
            max_sum = max_sum.max(f_node.val + b_node.val);
            head = f_node.next.take();
            back = b_node.next.take();
        }
        max_sum
    }
}

