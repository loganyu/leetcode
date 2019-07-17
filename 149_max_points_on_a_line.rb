=begin
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
=end

# @param {Integer[][]} points
# @return {Integer}
def max_points(points)
    n = points.length
    if n < 3
        return n
    end
    
    max_count = 1
    (0...n).each do |i|
        max_count = [max_points_on_a_line_containing_point_i(i, points, n), max_count].max
    end
    
    return max_count
end

def max_points_on_a_line_containing_point_i(i, points, n)
    lines = {}
    info = {
        :horizontal_lines => 1,
        :count => 1,
        :duplicates => 0,
    }
    (i+1...n).each do |j|
        add_line(i, j, lines, info, points)
    end
    return info[:count] + info[:duplicates]
end

def add_line(i, j, lines, info, points)
    x1, y1 = points[i]
    x2, y2 = points[j]
    
    if x1 == x2 && y1 == y2
        info[:duplicates] += 1
    elsif y1 == y2
        info[:horizontal_lines] += 1
        info[:count] =  [info[:count], info[:horizontal_lines]].max
    else
        slope = (x1 - x2) / (y1 - y2).to_f
        lines[slope] ||= 1
        lines[slope] += 1
        info[:count] =  [info[:count], lines[slope]].max
    end
end

