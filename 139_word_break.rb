=begin
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
=end

# @param {String} s
# @param {String[]} word_dict
# @return {Boolean}
def word_break(s, word_dict)
    word_dict = Hash[word_dict.map{|i| [i,true]}]
    memo = Array.new(s.length)
    
    return r_work_break(s, word_dict, 0, memo)
end

def r_work_break(s, word_dict, start, memo)
    if start == s.length
        return true
    end
    if !memo[start].nil?
        return memo[start]
    end
    (start + 1).upto(s.length).each do |i|
        if word_dict[s[start...i]] && r_work_break(s, word_dict, i, memo)
            return memo[start] = true
        end
    end
    
    return memo[start] = false
end