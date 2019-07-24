=begin
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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

# iterative solution
def inorder_traversal(root)
    res = []
    stack = []
    curr = root
    while !curr.nil? || !stack.empty?
        while !curr.nil?
            stack << curr
            curr = curr.left
        end
        curr = stack.pop
        res << curr.val
        curr = curr.right
    end
    
    return res
end
    
# recursive solution
def inorder_traversal(root)
    res = []
    if !root.nil?
        helper(root, res)
    end
    
    return res
end

def helper(root, res)
   if !root.left.nil?
       helper(root.left, res)
   end
   res << root.val
   if !root.right.nil?
       helper(root.right, res)
   end
end

