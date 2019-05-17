=begin
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
=end

# @param {String} s
# @param {String[]} dict
# @return {String}
def add_bold_tag(s, dict)
    intervals = []
    (0...s.length).each do |i|
        dict.each do |word|
            if s[i...i+word.length] == word
                intervals << [i, i + word.length - 1]
            end
        end
    end
    intervals = merge_intervals(intervals)
    
    (intervals.length-1).downto(0).each do |i|
        first_i = intervals[i][0]
        last_i = intervals[i][1]
        s.insert(last_i + 1, "</b>")
        s.insert(first_i, "<b>")
    end
    
    s
end

def merge_intervals(intervals)
    merged = []
    intervals.each do |interval|
        if merged.empty? || merged.last[1] + 1 < interval[0]
            merged << interval
        else
            if merged.last[1] < interval[1]
                merged.last[1] = interval[1]
            end
        end
    end    
    
    return merged
end

