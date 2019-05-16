=begin
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
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
def count_nodes(root)
    if root.nil?
        return 0
    end
    left_height = find_left_height(root)
    right_height = find_right_height(root)
    if left_height == right_height
        return (2**left_height) - 1
    else
        return 1 + count_nodes(root.left) + count_nodes(root.right)
    end
end

def find_left_height(node)
    h = 0
    while !node.nil?
        h += 1
        node = node.left
    end
    
    h
end

def find_right_height(node)
    h = 0
    while !node.nil?
        h += 1
        node = node.right
    end
    
    h
end

