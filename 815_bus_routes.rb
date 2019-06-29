=begin
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
=end

# @param {Integer[][]} routes
# @param {Integer} s
# @param {Integer} t
# @return {Integer}
def num_buses_to_destination(routes, s, t)
    if s == t
        return 0
    end  
    routes.map!{|route| Set.new(route)}
    graph = {}
    routes.length.times do |i|
        graph[i] = []
    end
    (0...routes.length).each do |i|
        (i+1...routes.length).each do |j|
            r1 = routes[i]
            r2 = routes[j]
            if !(r1 & r2).empty?
                graph[i] << j
                graph[j] << i
            end
        end
    end
    
    seen = Set.new
    targets = Set.new
    
    routes.each_with_index do |route, node|
        if route.include?(s)
            seen.add(node)
        end
        if route.include?(t)
            targets.add(node)
        end
    end
    
    queue = []
    seen.each do |node|
        queue << [node, 1]
    end

    while !queue.empty?
        node, depth = queue.shift
        
        if targets.include?(node)
            return depth
        end
        graph[node].each do |nei|
            if !seen.include?(nei)
                seen.add(nei)
                queue << [nei, depth+1]
            end
        end
    end
    
    return -1
end

