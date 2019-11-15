=begin
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
=end

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Boolean}
def is_valid_bst(root)
    if root.nil?
        return true
    end
    
    helper(root, nil, nil)
end

def helper(node, lower_limit, upper_limit)
    if lower_limit && node.val <= lower_limit
        return false
    end
    if upper_limit && node.val >= upper_limit
        return false
    end
    
    if node.left
        left = helper(node.left, lower_limit, node.val)
    else
        left = true
    end
    
    if left == false
        return false
    end
    
    if node.right
        right = helper(node.right, node.val, upper_limit)
    else
        right = true
    end
    
    return right
end
