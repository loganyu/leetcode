/*
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val == 0
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
var result int
var covered map[*TreeNode]bool

func minCameraCover(root *TreeNode) int {
    result = 0
    covered = map[*TreeNode]bool{}
    covered[nil] = true
    
    dfs(root, nil)
    
    return result
}

func dfs(node, parent *TreeNode) {
    if node != nil {
        dfs(node.Left, node)
        dfs(node.Right, node)
    
        if (parent == nil && !covered[node]) ||
            !covered[node.Left] ||
            !covered[node.Right] {
            result++
                covered[node] = true
                covered[parent] = true
                covered[node.Left] = true
                covered[node.Right] = true
        }
    }
}

