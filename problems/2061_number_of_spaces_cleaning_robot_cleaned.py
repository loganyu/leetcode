'''
A room is represented by a 0-indexed 2D binary matrix room where a 0 represents an empty space and a 1 represents a space with an object. The top left corner of the room will be empty in all test cases.

A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees clockwise and repeat this process. The starting space and all spaces that the robot visits are cleaned by it.

Return the number of clean spaces in the room if the robot runs indefinetely.



Example 1:




Input: room = [[0,0,0],[1,1,0],[0,0,0]]

Output: 7

Explanation:

​​​​​​​The robot cleans the spaces at (0, 0), (0, 1), and (0, 2).
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces down.
The robot cleans the spaces at (1, 2), and (2, 2).
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces left.
The robot cleans the spaces at (2, 1), and (2, 0).
The robot has cleaned all 7 empty spaces, so return 7.
Example 2:




Input: room = [[0,1,0],[1,0,0],[0,0,0]]

Output: 1

Explanation:

The robot cleans the space at (0, 0).
The robot hits an object, so it turns 90 degrees clockwise and now faces down.
The robot hits an object, so it turns 90 degrees clockwise and now faces left.
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces up.
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces right.
The robot is back at its starting position.
The robot has cleaned 1 space, so return 1.
Example 3:

Input: room = [[0,0,0],[0,0,0],[0,0,0]]

Output: 8​​​​​​​





Constraints:

m == room.length
n == room[r].length
1 <= m, n <= 300
room[r][c] is either 0 or 1.
room[0][0] == 0
'''

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        DIRECTIONS = (0, 1, 0, -1, 0)
        rows, cols = len(room), len(room[0])
        visited = set()
        cleaned = set()

        def clean(row, col, direction):
            if (row, col, direction) in visited:
                return len(cleaned)
            visited.add((row, col, direction))
            cleaned.add((row, col))
            next_row = row + DIRECTIONS[direction]
            next_col = col + DIRECTIONS[direction + 1]
            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and not room[next_row][next_col]
            ):
                return clean(next_row, next_col, direction)
            return clean(row, col, (direction + 1) % 4)

        return clean(0, 0, 0)

