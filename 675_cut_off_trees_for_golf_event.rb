=begin
You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
 

You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:

Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
 

Example 2:

Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
 

Example 3:

Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
 

Hint: size of the given matrix will not exceed 50x50.
=end

# BFS solution gives TLE error in Leetcode

# @param {Integer[][]} forest
# @return {Integer}
def cut_off_tree(forest)
    trees = []
    (0...forest.length).each do |r|
        (0...forest[0].length).each do |c|
            v = forest[r][c]
            if v > 1
                trees << [v, r, c]
            end
        end
    end
    sr = sc = ans = 0
    trees.sort_by!{|t| t[0]}
    trees.each do |_,tr,tc|
        d = dist(forest, sr, sc, tr, tc)
        if d < 0
            return -1
        end
        ans += d
        sr, sc = tr, tc
    end
    
    return ans
end

def dist(forest, sr, sc, tr, tc)
    h, w = forest.length, forest[0].length
    queue = [[sr,sc,0]]
    seen = Set.new([[sr,sc]])
    while !queue.empty?
        r, c, d = queue.shift
        if r == tr && c == tc
            return d
        end
        [[r-1,c],[r+1,c],[r,c-1],[r,c+1]].each do |nr, nc|
            if nr.between?(0,h-1) && nc.between?(0,w-1) &&
                !seen.include?([nr,nc]) &&
                forest[nr][nc] != 0
                seen.add([nr,nc])
                queue << [nr, nc, d+1]
            end
        end
    end
    
    return -1
end

