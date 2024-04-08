'''
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.



Example 1:


Input: preorder = [5,2,1,3,6]
Output: true
Example 2:

Input: preorder = [5,2,6,1,3]
Output: false


Constraints:

1 <= preorder.length <= 104
1 <= preorder[i] <= 104
All the elements of preorder are unique.


Follow up: Could you do it using only constant space complexity?
'''

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -inf
        i = 0

        for num in preorder:
            while i > 0 and preorder[i - 1] < num:
                min_limit = preorder[i - 1]
                i -= 1

            if num <= min_limit:
                return False

            preorder[i] = num
            i += 1

        return True

