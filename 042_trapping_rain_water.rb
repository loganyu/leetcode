=begin
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
=end

# @param {Integer[]} height
# @return {Integer}
def trap(height)
    if height.empty?
        return 0
    end
    ans = 0
    length = height.length
    left_max = []
    right_max = []
    left_max[0] = height[0]
    1.upto(length - 1).each do |i|
        left_max[i] = [left_max[i-1], height[i]].max
    end
    right_max[length - 1] = height[length - 1]
    (length - 2).downto(0).each do |i|
        right_max[i] = [right_max[i+1], height[i]].max
    end
    1.upto(length - 2).each do |i|
        ans += [left_max[i], right_max[i]].min - height[i]
    end
    
    ans
end