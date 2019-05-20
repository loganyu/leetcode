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
    largest_overall = [largest_overall, largest].max
  end
  
  return largest_overall
end


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