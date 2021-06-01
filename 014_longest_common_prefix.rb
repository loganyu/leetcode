=begin
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
=end

# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    prefix = ''
    i = 0
    if strs.empty?
        return prefix
    end
    loop do
        if strs.any?{|s|s[i].nil?}
            break
        end
        char = strs[0][i]
        if strs.all?{|s| s[i] == char}
            prefix += char
        else
            break
        end
        i += 1
    end
    
    prefix
end
