=begin
# @param {Integer[][]} points
# @return {Integer}
def min_area_rect(points)
    columns = {}
    points.each do |x,y|
        columns[x] ||= []
        columns[x] << y
    end
    last_x = {}
    ans = Float::INFINITY
    columns.keys.sort.each do |x|
        column = columns[x].sort
        column.each_with_index do |y2, i|
            (0...i).each do |j|
                y1 = column[j]
                if last_x[[y1, y2]]
                    ans = [ans, (x - last_x[[y1,y2]]) * (y2 - y1)].min
                end
                last_x[[y1,y2]] = x
            end
        end
    end
    if ans == Float::INFINITY
        return 0
    else
        return ans
    end
end
=end

# @param {Integer[][]} points
# @return {Integer}
def min_area_rect(points)
    columns = {}
    points.each do |x, y|
        columns[x] ||= []
        columns[x] << y
    end
    
    min = Float::INFINITY
    last_x = {}
    columns.keys.sort.each do |x2|
        column = columns[x2].sort
        (0...column.length-1).each do |i|
            (i+1...column.length).each do |j|
                y1 = column[i]
                y2 = column[j]
                if last_x[[y1,y2]]
                    x1 = last_x[[y1,y2]]
                    area = (x2 - x1) * (y2 - y1)
                    min = [min, area].min
                end
                last_x[[y1,y2]] = x2
            end
        end
    end
    
    return min == Float::INFINITY ? 0 : min
end

=begin
Runtime error when using diagonals approach
# @param {Integer[][]} points
# @return {Integer}
def min_area_rect(points)
    set = Set.new(points)
    ans = Float::INFINITY
    (0...points.length).each do |i|
        (0...i).each do |j|
            p1 = points[i]
            p2 = points[j]
            if p1[0] != p2[0] && p1[1] != p2[1] && 
                set.include?([p1[0], p2[1]]) && set.include?([p2[0], p1[1]])
                ans = [ans, (p2[0] - p1[0]).abs * (p2[1] - p1[1]).abs].min
            end
        end
    end
    
    if ans == Float::INFINITY
        return 0
    else
        return ans
    end         
end
=end

