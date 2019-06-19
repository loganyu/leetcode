=begin
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
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
def longest_consecutive(root)
    @max_length = 0
    dfs(root, nil, 0)
    
    return @max_length
end

def dfs(node, parent, length)
    if node.nil?
        return
    end
    if !parent.nil? && node.val == parent.val + 1
        length += 1
    else
        length = 1
    end
    @max_length = [@max_length, length].max
    dfs(node.right, node, length)
    dfs(node.left, node, length)
end

