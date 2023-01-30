'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''
# O(n) space and O(n^2) time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.find_paths(root, sum) + self.pathSum(root.right, sum) + self.pathSum(root.left, sum)
        
    def find_paths(self, root, sum):
        if not root:
            return 0
        return int(root.val == sum) + self.find_paths(root.left, sum - root.val) + self.find_paths(root.right, sum - root.val)

# O(n) space and O(n) time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, prevSum):
            if not root:
                return
            currSum = prevSum + root.val
            if currSum - sum in countBySum:
                self.count += countBySum[currSum - sum]
            if currSum in countBySum:
                countBySum[currSum] += 1
            else:
                countBySum[currSum] = 1
            
            dfs(root.left, currSum)
            dfs(root.right, currSum)
            countBySum[currSum] -= 1
            
        self.count = 0
        countBySum = {0:1}
        dfs(root, 0)
        
        return self.count
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        memo = defaultdict(int)
        memo[0] = 1
        
        return self.find_paths(root, 0, targetSum, memo)
        
    def find_paths(self, curr, currSum, targetSum, memo):
        if not curr:
            return 0
        currSum += curr.val
        numPathsToCurr = memo[currSum - targetSum]
        memo[currSum] += 1
        res = numPathsToCurr + self.find_paths(curr.left, currSum, targetSum, memo) + self.find_paths(curr.right, currSum, targetSum, memo)
        memo[currSum] -= 1
        
        return res

