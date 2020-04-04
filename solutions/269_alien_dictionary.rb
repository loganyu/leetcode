=begin
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
=end

require 'set'

# @param {String[]} words
# @return {String}
def alien_order(words)
    if words.nil? || words.empty?
        return ''
    end
    
    map = {}
    degrees = {}
    result = ''
    
    words.each do |word|
        word.each_char do |char|
            degrees[char] = 0
        end
    end
    
    0.upto(words.length - 2).each do |i|
        word1 = words[i]
        word2 = words[i+1]
        if word1 == word2
            next
        end
        if word1.start_with?(word2)
            return ""
        end
        length = [word1.length, word2.length].min
        0.upto(length - 1).each do |j|
            c1 = word1[j]
            c2 = word2[j]
            if c1 != c2
                map[c1] ||= Set.new
                if !map[c1].include?(c2)
                    map[c1].add(c2)
                    degrees[c2] += 1
                end
                break
            end
        end
    end
    
    queue = degrees.select{|c, degrees| degrees == 0}.keys
    while !queue.empty?
        c = queue.shift
        result += c
        if map[c]
            map[c].each do |c2|
                degrees[c2] -= 1
                if degrees[c2] == 0
                    queue.push(c2)
                end
            end
        end
    end
    
    if result.length != degrees.length
        return ''
    else
        return result
    end
end
