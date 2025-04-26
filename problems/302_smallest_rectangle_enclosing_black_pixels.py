'''
You are given an m x n binary matrix image where 0 represents a white pixel and 1 represents a black pixel.

The black pixels are connected (i.e., there is only one black region). Pixels are connected horizontally and vertically.

Given two integers x and y that represents the location of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

You must write an algorithm with less than O(mn) runtime complexity



Example 1:


Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
Output: 6
Example 2:

Input: image = [["1"]], x = 0, y = 0
Output: 1


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 100
image[i][j] is either '0' or '1'.
0 <= x < m
0 <= y < n
image[x][y] == '1'.
The black pixels in the image only form one component.
'''

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        left = right = y
        top = bottom = x

        for r in range(m):
            for c in range(n):
                if image[r][c] == "0": continue
                left = min(left, c)
                right = max(right, c)
                top = min(top, r)
                bottom = max(bottom, r)
        return (bottom - top + 1) * (right - left + 1)

