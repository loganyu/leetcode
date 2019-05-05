=begin
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
=end

# @param {Integer[]} height
# @return {Integer}
def max_area(height)
    i, j = 0, height.length - 1
    area = 0
    while i < j
        area = [area, (j - i)*[height[i], height[j]].min].max
        height[i] < height[j] ? i+=1 : j-=1
    end
    
    area
end