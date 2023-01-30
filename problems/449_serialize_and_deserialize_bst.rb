=begin
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary search tree can be serialized to a string and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
=end

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# Encodes a tree to a single string.
#
# @param {TreeNode} root
# @return {string}
def serialize(root)
    rserialize(root, "")
end

def rserialize(node, string)
    if node.nil?
        return string
    end
    string += "#{node.val},"
    string = rserialize(node.left, string)
    string = rserialize(node.right, string)
end

# Decodes your encoded data to tree.
#
# @param {string} data
# @return {TreeNode}
def deserialize(data)
    list = data.split(",")
    rdeserialize(list, -Float::INFINITY, Float::INFINITY)
end

def rdeserialize(l, lower, upper)
    if l[0].nil?
        return nil
    end
    val = l[0].to_i
    if val < lower || val > upper
        return nil
    end
    l.shift
    root = TreeNode.new(val)
    root.left = rdeserialize(l, lower, val)
    root.right = rdeserialize(l, val, upper)
    
    return root
end


# Your functions will be called as such:
# deserialize(serialize(data))
