=begin
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
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
# @return {Integer[]}
def right_side_view(root)
    rightmost_value_at_depth = {}
    max_depth = -1
    
    stack = [[root, 0]]
    
    while !stack.empty?
        node, depth = stack.pop
        if !node.nil?
            max_depth = [max_depth, depth].max

            rightmost_value_at_depth[depth] ||= node.val

            stack.push([node.left, depth + 1])
            stack.push([node.right, depth + 1])
        end
    end
    
    (0..max_depth).map{|depth| rightmost_value_at_depth[depth]}
end

