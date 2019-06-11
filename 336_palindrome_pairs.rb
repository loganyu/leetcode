=begin
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
=end

# @param {String[]} words
# @return {Integer[][]}
def palindrome_pairs(words)
    pairs = []
    index_by_word = {}
    words.each_with_index do |word, i|
        index_by_word[word] = i
    end
    words.each do |word|
        wl = word.length
        (0..wl).each do |i|
            pref = word[0...i]
            suf = word[i...wl]
            if is_palindrome?(pref)
                back = suf.reverse
                if back != word && index_by_word[back]
                    pairs << [index_by_word[back], index_by_word[word]]
                end
            end
            if i != wl && is_palindrome?(suf)
                back = pref.reverse
                if back != word && index_by_word[back]
                    pairs << [index_by_word[word], index_by_word[back]]
                end
            end
        end
    end
    
    return pairs
end

def is_palindrome?(word)
    word == word.reverse
end

