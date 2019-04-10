=begin
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
=end

# @param {Integer[][]} points
# @param {Integer} k
# @return {Integer[][]}
def k_closest(points, k)
    dists = points
    sort(0, points.length - 1, k, points)
    return points[0...k]
end

def sort(i, j, k, points)
    if i >= j
        return
    end
    
    r = rand(i..j)
    points[i], points[r] = points[r], points[i]

    mid = partition(i, j, points)
    left_length = mid - i + 1
    if k < left_length
        sort(i, mid - 1, k, points)
    elsif k > left_length
        sort(mid + 1, j, k - left_length, points)
    end
end

def partition(i, j, points)
    oi = i
    pivot = dist(i, points)
    i += 1
    
    loop do
        while i < j && dist(i, points) <= pivot
            i += 1
        end
        while i <= j && dist(j, points) >= pivot
            j -= 1
        end
        if i >= j
            break
        end
        points[i], points[j] = points[j], points[i]
    end
    points[oi], points[j] = points[j], points[oi]
    
    return j
end

def dist(i, points)
   Math.sqrt(points[i][0]**2 + points[i][1]**2)
end
