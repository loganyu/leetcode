=begin
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
=end

# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
    map = {}
    degree = {}
    num_courses.times do |course|
        degree[course] = 0
    end
    
    prerequisites.each do |course, prereq|
        map[prereq] ||= Set.new
        map[prereq].add(course)
        degree[course] += 1
    end
    
    count = 0
    queue = []
    degree.each do |course, degrees|
        if degrees == 0
            queue << course
        end
    end
    while !queue.empty?
        prereq = queue.shift
        count += 1
        if map[prereq]
            map[prereq].each do |course|
                degree[course] -= 1
                if degree[course] == 0
                    queue << course
                end
            end
        end
    end
    
    return count == num_courses
end

