=begin
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
=end

# @param {Integer[]} seats
# @return {Integer}
def max_dist_to_closest(seats)
    left = -1
    right = 0
    max = 0
    n = seats.length
    seats.each_with_index do |seat, i|
        if seat == 1
            left = i
        else
            while right < n && seats[right] == 0 || right < i
                right += 1
            end
            left_dist = left == -1 ? n : i - left
            right_dist = right == n ? n : right - i
            
            max = [max, [left_dist, right_dist].min].max
        end
    end
    
    return max
end

