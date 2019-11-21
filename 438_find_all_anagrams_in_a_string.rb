=begin
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
=end

# @param {String} s
# @param {String} p
# @return {Integer[]}
def find_anagrams(s, p)
    res = []
    p_count = {}
    p.each_char do |char|
        p_count[char] ||= 0
        p_count[char] += 1
    end
    s_count = {}
    s[0...p.length-1].each_char do |char|
        s_count[char] ||= 0
        s_count[char] += 1
    end
    
    (p.length-1).upto(s.length-1).each do |i|
        s_count[s[i]] ||= 0
        s_count[s[i]] += 1
        start_index = i - p.length + 1
        if s_count == p_count
            res.push(start_index)
        end
        s_count[s[start_index]] -= 1
        if s_count[s[start_index]] == 0
            s_count.delete(s[start_index])
        end
    end
    
    return res
end

