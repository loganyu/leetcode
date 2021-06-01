=begin
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
=end

require 'set'

# @param {String} s
# @param {String[]} word_dict
# @return {String[]}
def word_break(s, word_dict)
    @word_dict = Set.new(word_dict)
    @memo = {}
    @s = s
    return recurse(0)
end

def recurse(start)
    if @memo[start]
        return @memo[start]
    end
    res = []
    if start == @s.length
        res << ''
    end
    (start+1).upto(@s.length).each do |en|
        if @word_dict.include?(@s[start...en])
            cur_res = recurse(en)
            cur_res.each do |item|
                if item == ''
                    res << @s[start...en]
                else
                    res << "#{@s[start...en]} #{item}"
                end
            end
        end
    end
    @memo[start] = res
    
    return res
end

