=begin
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
=end

# @param {Integer} n
# @return {Integer[][]}
def generate_matrix(n)
    if n <= 0
      return []
    end
    matrix = Array.new(n) {Array.new(n)}

    # right, down, left, up directions
    dir_c = [1,0,-1,0]
    dir_r = [0,1,0,-1]
    # 0, 1, 2, 3 = right, down, left, up directions
    dir = 0
    r = 0
    c = 0
    limit = n**2
    val = 1
    matrix[r][c] = val
    loop do
      if val >= limit
          break
      end
      r += dir_r[dir]
      c += dir_c[dir]
      if is_invalid?(matrix, r, c)
        r -= dir_r[dir]
        c -= dir_c[dir]
        dir = (dir+1)%4
        r += dir_r[dir]
        c += dir_c[dir]
      end
      val += 1
      matrix[r][c] = val
    end

    return matrix
end

def is_invalid?(m, r, c)
  return r < 0 || 
      c < 0 ||
      r >= m.length ||
      c >= m.length ||
      !m[r][c].nil?
end

generate_matrix(5).each do |r|
  puts r.inspect
end