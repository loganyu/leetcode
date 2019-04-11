=begin
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

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
    rserialize(root, '')
end

def rserialize(root, string)
    if root.nil?
        string += 'nil,'
    else
        string += "#{root.val},"
        string = rserialize(root.left, string)
        string = rserialize(root.right, string)
    end
    
    return string
end


# Decodes your encoded data to tree.
#
# @param {string} data
# @return {TreeNode}
def deserialize(data)
    data_list = data.split(',')
    root = rdeserialize(data_list)
    
    return root
end

def rdeserialize(l)
    if l[0] == 'nil'
        l.shift
        return nil
    end
    root = TreeNode.new(l.shift)
    root.left = rdeserialize(l)
    root.right = rdeserialize(l)
    
    return root
end


# Your functions will be called as such:
# deserialize(serialize(data))

