=begin
Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
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
    @max = 0
    longest_path(root)
    
    return @max
end

def longest_path(node)
    if node.nil?
        return [0,0]
    end
    inr = 1
    dcr = 1
    if node.left
        l = longest_path(node.left)
        if node.val == node.left.val + 1
            dcr = l[1] + 1
        elsif node.val == node.left.val - 1
            inr = 1[0] + 1
        end
    end
    if node.right
        r = longest_path(node.right)
        if node.val = node.right.val + 1
            dcr = [dcr, r[1] + 1].max
        elsif node.val == node.right.val - 1
            inr = [inr, r[0] + 1].max
        end
    end
    @max = [@max, dcr + inr - 1].max
    
    return [inr, dcr]
end

