=begin
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.
 
Example:

Input: [2,1,5,6,2,3]
Output: 10
=end

# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
  stack = []
  max_area = 0
  i = 0
  while i < heights.length
    if stack.empty? || heights[stack.last] <= heights[i]
      stack.push(i)
      i += 1
    else
      max_area = pop_from_stack_and_get_max_area(stack, heights, i, max_area)
    end
  end
  while !stack.empty?
    max_area = pop_from_stack_and_get_max_area(stack, heights, i, max_area)
  end
    
  return max_area
end

def pop_from_stack_and_get_max_area(stack, heights, i, max_area)
    top = stack.pop()
    if stack.empty?
      area = heights[top] * i
    else
      area = heights[top] * (i - stack.last - 1)
    end
    
    return [max_area, area].max
end