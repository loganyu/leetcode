=begin
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
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
def level_order(root)
    @levels = []
    if root.nil?
        return @levels
    end
    
    helper(root, 0)
    
    return @levels
end

def helper(node, level)
    if @levels.length == level
        @levels.push([])
    end
    
    @levels[level] << node.val
    
    if !node.left.nil?
        helper(node.left, level + 1)
    end
    if !node.right.nil?
        helper(node.right, level + 1)
    end
end

