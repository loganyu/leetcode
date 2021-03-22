'''
Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in strictly increasing order.
'''

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        pos = [0] * n
        curr_max = 0
        count = 0
        while True:
            for i in range(n):
                while pos[i] < m and mat[i][pos[i]] < curr_max:
                    pos[i] += 1
                if pos[i] >= m:
                    return -1
                if mat[i][pos[i]] != curr_max:
                    count = 1
                    curr_max = mat[i][pos[i]]
                else:
                    count += 1
                    if count == n:
                        return curr_max
                    
