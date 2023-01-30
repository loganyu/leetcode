/*
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private ListNode head;
    
    private TreeNode convert(int l, int r) {
        if (l > r) {
            return null;
        }
        int mid = (l + r) / 2;
        
        TreeNode left = this.convert(1, mid - l);
        TreeNode node = new TreeNode(this.head.val);
        node.left = left;
        
        this.head = this.head.next;
        
        node.right = this.convert(mid + 1, r);
        
        return node;
    }
    
    public TreeNode sortedListToBST(ListNode head) {
        int size = 0;
        ListNode ptr = head;
        while (ptr != null) {
            ptr = ptr.next;
            size += 1;
        }
        
        this.head = head;
        
        return convert(0, size - 1);
    }
}

