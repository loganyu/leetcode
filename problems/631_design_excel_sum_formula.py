'''
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").


Example 1:

Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]

Explanation
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] and the values sum of the rectangle range whose top-left cell is mat[1]["A"] and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6


Constraints:

1 <= height <= 26
'A' <= width <= 'Z'
1 <= row <= height
'A' <= column <= width
-100 <= val <= 100
1 <= numbers.length <= 5
numbers[i] has the format "ColRow" or "ColRow1:ColRow2".
At most 100 calls will be made to set, get, and sum.
'''

class Excel:

    def __init__(self, height: int, width: str):
        self.w = ord(width) - ord('A') + 1
        self.h = height
        self.grid = [[ [0, {}] for _ in range(self.w)] for _ in range(self.h)]

    def _get_coords(self, row: int, column: str):
        return row - 1, ord(column) - ord('A')

    def set(self, row: int, column: str, val: int) -> None:
        r, c = self._get_coords(row, column)
        self.grid[r][c] = [val, {}]
        self._update_dependencies()


    def get(self, row: int, column: str) -> int:
        r, c = self._get_coords(row, column)
        return self.grid[r][c][0]


    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r, c = self._get_coords(row, column)

        dep_map = collections.defaultdict(int)
        for s in numbers:
            if ":" not in s:
                dep_map[s] += 1
            else:
                start, end = s.split(":")
                r1, c1 = int(start[1:]), ord(start[0])
                r2, c2 = int(end[1:]), ord(end[0])
                for i in range(r1, r2 + 1):
                    for j_code in range(c1, c2 + 1):
                        cell_name = f"{chr(j_code)}{i}"
                        dep_map[cell_name] += 1

        self.grid[r][c][1] = dict(dep_map)
        return self._update_dependencies(r, c)

    def _update_dependencies(self, target_r=None, target_c=None):
        changed = True
        while changed:
            changed = False
            for r in range(self.h):
                for c in range(self.w):
                    val, deps = self.grid[r][c]
                    if deps:
                        new_val = 0
                        for cell_name, count in deps.items():
                            dr, dc = self._get_coords(int(cell_name[1:]), cell_name[0])
                            new_val += self.grid[dr][dc][0] * count

                        if new_val != val:
                            self.grid[r][c][0] = new_val
                            changed = True

        if target_r is not None:
            return self.grid[target_r][target_c][0]



# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
