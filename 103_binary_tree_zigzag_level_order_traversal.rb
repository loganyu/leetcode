=begin
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
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
# @return {Integer[][]}
def zigzag_level_order(root)
    if root.nil?
        return []
    end
    levels = []
    reverse = false
    queue = [root]
    while !queue.empty?
        next_queue = []
        level = []
        queue.each do |node|
            reverse ? level.unshift(node.val) : level.push(node.val)
            next_queue << node.left if node.left
            next_queue << node.right if node.right
        end
        queue = next_queue
        levels << level
        reverse = !reverse
    end
    
    levels
end

