=begin
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
=end

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right, = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} target
# @param {Integer} k
# @return {Integer[]}
def distance_k(root, target, k)
    parent_by_node = {}
    dfs(root, nil, parent_by_node)
    queue = [[target,0]]
    seen = Set.new([target])
    while !queue.empty?
        if queue[0][1] == k
            return queue.map{|n, d| n.val}
        end
        node, d = queue.shift
        [node.left, node.right, parent_by_node[node]].each do |nei|
            if nei && !seen.include?(nei)
                seen.add(nei)
                queue << [nei, d+1]
            end
        end
    end
    
    return []
end
    
def dfs(node, parent, parent_by_node)
    if node
        parent_by_node[node] = parent
        dfs(node.left, node, parent_by_node)
        dfs(node.right, node, parent_by_node)
    end
end

