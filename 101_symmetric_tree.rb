# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Boolean}
def is_symmetric(root)
    return is_mirror(root, root)
end

def is_mirror(t1, t2)
  if t1.nil? && t2.nil?
    return true
  end
  if t1.nil? || t2.nil?
    return false
  end
  return (t1.val == t2.val) && is_mirror(t1.left, t2.right) && is_mirror(t1.right, t2.left)
end
