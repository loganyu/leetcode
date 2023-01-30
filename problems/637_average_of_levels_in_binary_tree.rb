=begin
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
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
# @return {Float[]}
def average_of_levels(root)
    count = []
    sum = []
    average(root, 0, sum, count)
    (0...sum.length).each do |i|
        sum[i] = sum[i]/count[i].to_f
    end
    
    sum
end

def average(node, level, sum, count)
    if node.nil?
        return
    end
    if level < sum.length
        sum[level] += node.val
        count[level] += 1
    else
        sum << node.val
        count << 1
    end
    
    average(node.left, level+1, sum, count)
    average(node.right, level+1, sum, count)
end

