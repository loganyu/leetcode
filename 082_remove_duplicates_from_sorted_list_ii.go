/*
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
*/

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
	prehead := &ListNode{0, head}
	pre := prehead
	cur := head
	for cur != nil {
		if cur.Next == nil || cur.Val != cur.Next.Val {
			if pre.Next == cur {
				pre = cur
			} else {
				pre.Next = cur.Next
			}
		}
		cur = cur.Next
	}
	return prehead.Next
}
