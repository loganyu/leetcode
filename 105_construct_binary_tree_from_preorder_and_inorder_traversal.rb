=begin
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
=end

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} preorder
# @param {Integer[]} inorder
# @return {TreeNode}
def build_tree(preorder, inorder)
    @idx_map = {}
    @pre_idx = 0
    @preorder = preorder
    @inorder = inorder
    inorder.each_with_index do |val, i|
        @idx_map[val] = i
    end
    
    return helper(0, inorder.length)
end

def helper(in_left, in_right)
    if in_left == in_right
        return nil
    end
    
    root_val = @preorder[@pre_idx]
    root = TreeNode.new(root_val)
    
    index = @idx_map[root_val]
    @pre_idx += 1
    root.left = helper(in_left, index)
    root.right = helper(index + 1, in_right)
    
    return root
end

