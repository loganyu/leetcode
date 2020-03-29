=begin
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
=end

# @param {String} j
# @param {String} s
# @return {Integer}
def num_jewels_in_stones(j, s)
    jewels = {}
    j.each_char do |jewel|
        jewels[jewel] = true
    end
    jewel_count = 0
    s.each_char do |stone|
        if jewels[stone]
            jewel_count += 1
        end
    end
    
    jewel_count
end