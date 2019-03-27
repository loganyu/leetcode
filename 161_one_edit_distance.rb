=begin
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
=end

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_one_edit_distance(s, t)
    ns, nt = s.length, t.length
    if ns > nt
        return is_one_edit_distance(t, s)
    end
    
    if nt - ns > 1
        return false
    end
    
    0.upto(ns-1) do |i|
        if s[i] != t[i]
            if ns == nt
                return s[i+1..-1] == t[i+1..-1]
            else
                return s[i..-1] == t[i+1..-1]
            end
        end
    end
    
    return ns + 1 == nt
end