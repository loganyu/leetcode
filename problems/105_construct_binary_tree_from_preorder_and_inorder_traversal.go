/*
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 || len(inorder) == 0 { return nil }
    return helper(&preorder, &inorder, 0, 0, len(preorder)-1)
}

func helper(preorder, inorder *[]int, preStart, inStart, inEnd int) *TreeNode {
    if preStart > len(*preorder) || inStart > inEnd {
        return nil
    }
    current := &TreeNode{Val: (*preorder)[preStart]}
    i := inStart
    for i <= inEnd {
        if (*inorder)[i] == (*preorder)[preStart] { break }
        i++
    }
    current.Left = helper(preorder, inorder, preStart+1, inStart, i-1)
    current.Right = helper(preorder, inorder, preStart+(i-inStart+1), i+1, inEnd)
    return current
}

