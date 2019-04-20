=begin
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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
# @return {Integer}
def max_path_sum(root)
    @max_sum = -Float::INFINITY
    max_gain(root)
    
    return @max_sum
end

def max_gain(node)
    if node.nil?
        return 0
    end
        
    left_gain = [max_gain(node.left), 0].max
    right_gain = [max_gain(node.right), 0].max
    price_newpath = node.val + left_gain + right_gain
    @max_sum = [@max_sum, price_newpath].max
    
    return node.val + [left_gain, right_gain].max
end
