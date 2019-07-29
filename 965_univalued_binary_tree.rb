=begin
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

 

Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false
 

Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
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
def is_unival_tree(root)
    if root.nil?
        return true
    end
    val = root.val
    
    return dfs(root, val)
end

def dfs(node, val)
    if node.nil?
        return true
    end
    
    return node.val == val && dfs(node.left, val) && dfs(node.right, val)
end

