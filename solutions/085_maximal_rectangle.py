'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

# histograms stack. O(NM) time and O(M) spaceoclass Solution:


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_area = 0
        heights = [0]*len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                area = heights[stack.pop()] * (i - stack[-1] - 1)
                max_area = max(max_area, area)
            stack.append(i)
        while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
            area = heights[stack.pop()] * (len(heights) - stack[-1] - 1)
            max_area = max(max_area, area)

        return max_area

# max height at each point. O(NM) time and O(M) space


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        maxarea = 0

        for r in range(m):
            cur_left, cur_right = 0, n
            for c in range(n):
                if matrix[r][c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
            for c in range(n):
                if matrix[r][c] == '1':
                    left[c] = max(left[c], cur_left)
                else:
                    left[c] = 0
                    cur_left = c + 1
            for c in reversed(range(n)):
                if matrix[r][c] == '1':
                    right[c] = min(right[c], cur_right)
                else:
                    right[c] = n
                    cur_right = c
            for c in range(n):
                maxarea = max(maxarea, height[c] * (right[c] - left[c]))

        return maxarea
