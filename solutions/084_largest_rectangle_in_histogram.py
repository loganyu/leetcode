'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        i = 0
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                max_area = self.pop_from_stack_and_get_max_area(stack, heights, i, max_area)
        while len(stack) > 0:
            max_area = self.pop_from_stack_and_get_max_area(stack, heights, i, max_area)
        
        return max_area
    
    def pop_from_stack_and_get_max_area(self, stack, heights, i, max_area):
        top = stack.pop()
        if len(stack) == 0:
            area = heights[top] * i
        else:
            area = heights[top] * (i - stack[-1] - 1)
        
        return max(max_area, area)

