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
    sol = []
    if root.nil?
        return sol
    end
    queue = [root]
    while !queue.empty?
        num_items_at_level = queue.length
        num_items_at_level.times do |i|
            cur = queue.shift
            queue.push(cur.left) if cur.left
            queue.push(cur.right) if cur.right
            if i == num_items_at_level - 1
                sol.push(cur.val)
            end
        end
    end
    
    return sol
end
