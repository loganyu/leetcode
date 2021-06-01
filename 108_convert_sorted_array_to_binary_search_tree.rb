=begin
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
=end

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} nums
# @return {TreeNode}
def sorted_array_to_bst(nums)
    return convert(nums, 0, nums.length - 1)
end

def convert(nums, left, right)
    if left > right
        return nil
    end
    mid = left + (right - left)/2
    node = TreeNode.new(nums[mid])
    node.left = convert(nums, left, mid - 1)
    node.right = convert(nums, mid + 1, right)
    
    return node
end

