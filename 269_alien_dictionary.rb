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

# @param {String[]} words
# @return {String}
def alien_order(words)
    map = {}
    degree = {}
    result = ""
    
    if words.nil? || words.empty?
        return result
    end
    
    words.each do |word|
        word.each_char do |char|
            degree[char] = 0
        end
    end
    
    0.upto(words.length - 2).each do |i|
        cur = words[i]
        nex = words[i+1]
        length = [cur.length, nex.length].min
        0.upto(length - 1).each do |j|
            c1 = cur[j]
            c2 = nex[j]
            if c1 != c2
                map[c1] ||= Set.new
                map[c1].add(c2)
                degree[c2] += 1
                break
            end
        end
    end
    
    queue = []
    degree.each do |char, degrees|
       if degrees == 0
           queue.push(char)
       end
    end
    
    while !queue.empty?
        c = queue.shift
        result += c
        if map[c]
            map[c].each do |c2|
                degree[c2] -= 1
                if degree[c2] == 0
                    queue.push(c2)
                end
            end
        end
    end
    
    if result.length != degree.length
        return ""
    end
    
    return result
end
