# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
  if matrix.length == 0
    return 0
  end
  histogram = Array.new(matrix[0].length){0}
  largest_overall = 0
  matrix.each do |row|
    row.each_with_index do |num, i|
      if num == "0"
        histogram[i] = 0
      elsif num == "1"
        histogram[i] += 1
      end
    end
    
    largest = largest_rectangle_area(histogram)
    if largest > largest_overall
      largest_overall = largest
    end
  end
  
  return largest_overall
end


=begin
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
=end

# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
  stack = []
  max_area = 0
  area = 0
  i = 0
  while i < heights.length do
    if stack.empty? || heights[stack.last] <= heights[i]
      stack.push(i)
      i += 1
    else
      top = stack.pop()
      if stack.empty?
        area = heights[top] * i
      else
        area = heights[top] * (i - stack.last - 1)
      end
      if area > max_area
        max_area = area
      end
    end
  end
  while !stack.empty?
    top = stack.pop()
    if stack.empty?
      area = heights[top] * i
    else
      area = heights[top] * (i - stack.last - 1)
    end
    if area > max_area
      max_area = area
    end
  end
    
  return max_area
end