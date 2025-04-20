'''
If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. For each integer in this array:

The hundreds digit represents the depth d of this node where 1 <= d <= 4.
The tens digit represents the position p of this node in the level it belongs to where 1 <= p <= 8. The position is the same as that in a full binary tree.
The units digit represents the value v of this node where 0 <= v <= 9.
Given an array of ascending three-digit integers nums representing a binary tree with a depth smaller than 5, return the sum of all paths from the root towards the leaves.

It is guaranteed that the given array represents a valid connected binary tree.



Example 1:


Input: nums = [113,215,221]
Output: 12
Explanation: The tree that the list represents is shown.
The path sum is (3 + 5) + (3 + 1) = 12.
Example 2:


Input: nums = [113,221]
Output: 4
Explanation: The tree that the list represents is shown.
The path sum is (3 + 1) = 4.


Constraints:

1 <= nums.length <= 15
110 <= nums[i] <= 489
nums represents a valid binary tree with depth less than 5.

'''

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        map = (
            {}
        )
        for element in nums:
            coordinates = element // 10
            value = element % 10
            map[coordinates] = value

        total_sum = 0
        q = [
            (nums[0] // 10, map[nums[0] // 10])
        ]
        while q:
            coordinates, current_sum = q.pop(0)
            level = coordinates // 10
            position = coordinates % 10

            left = (level + 1) * 10 + position * 2 - 1
            right = (level + 1) * 10 + position * 2

            if not (left in map or right in map):
                total_sum += current_sum

            if left in map:
                q.append((left, current_sum + map[left]))

            if right in map:
                q.append((right, current_sum + map[right]))

        return total_sum

