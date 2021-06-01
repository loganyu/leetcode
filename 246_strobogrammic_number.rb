=begin
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
=end

# @param {String} num
# @return {Boolean}
def is_strobogrammatic(num)
    map = {
        "6" => "9",
        "9" => "6",
        "8" => "8",
        "0" => "0",
        "1" => "1",
    }
    (0..num.length/2).each do |i|
       if num[i] != map[num[num.length - 1 - i]]
           return false
       end
    end
    
    return true
end
