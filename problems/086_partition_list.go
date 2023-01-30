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

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func partition(head *ListNode, x int) *ListNode {
    before, after := &ListNode{-1, nil}, &ListNode{-1, nil}
    beforeHead, afterHead := before, after

	for head != nil {
		if head.Val < x {
			before.Next = head
            before = before.Next
		} else {
            after.Next = head
            after = after.Next
		}
        head = head.Next
	}
    after.Next = nil
    before.Next = afterHead.Next

	return beforeHead.Next
}

