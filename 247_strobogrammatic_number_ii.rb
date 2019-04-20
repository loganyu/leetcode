=begin
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
=end

# @param {Integer} n
# @return {String[]}
def find_strobogrammatic(n)
    helper(n, n)
end

def helper(len, n)
    if len == 0
        return [""]
    end
    if len == 1
        return ["0", "1", "8"]
    end
    
    list = helper(len-2, n)
    ans = []
    (0...list.length).each do |i|
        if len != n
            ans << '0' + list[i] + '0'
        end
        ans << '1' + list[i] + '1'
        ans << '6' + list[i] + '9'
        ans << '8' + list[i] + '8'
        ans << '9' + list[i] + '6'
    end
    
    return ans
end