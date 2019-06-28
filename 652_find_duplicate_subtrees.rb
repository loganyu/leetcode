=begin
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
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
# @return {TreeNode[]}
def find_duplicate_subtrees(root)
    count = {}
    ans = []
    lookup(root, count, ans)
    
    return ans
end

def lookup(node, count, ans)
    if node.nil?
        return nil
    end
    
    uid = [node.val, lookup(node.left, count, ans), lookup(node.right, count, ans)]
    count[uid] ||= 0
    count[uid] += 1
    if count[uid] == 2
        ans << node
    end

    return uid
end
