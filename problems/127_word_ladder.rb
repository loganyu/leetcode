=begin
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
=end

# @param {String} begin_word
# @param {String} end_word
# @param {String[]} word_list
# @return {Integer}
require 'set'

def ladder_length(begin_word, end_word, word_list)
    if !word_list.include?(end_word) || end_word.empty? || begin_word.empty? || word_list.empty?
        return 0
    end
    l = begin_word.length
    all_combo_dict = {}
    word_list.each do |word|
        0.upto(l - 1).each do |i|
            generic_word = "#{word[0...i]}*#{word[i+1...l]}"
            all_combo_dict[generic_word] ||= []
            all_combo_dict[generic_word] << word
        end
    end
    
    queue = [[begin_word, 1]]
    visited = {begin_word => true}
    
    while !queue.empty?
        current_word, level = queue.shift
        0.upto(l - 1).each do |i|
            intermediate_word = "#{current_word[0...i]}*#{current_word[i+1...l]}"
            if all_combo_dict[intermediate_word]
                all_combo_dict[intermediate_word].each do |word|
                    if word == end_word
                        return level + 1
                    end
                    if !visited.include?(word)
                        visited[word] = true
                        queue.push([word, level + 1])
                    end
                end
                all_combo_dict[intermediate_word] = nil
            end
        end
    end
    
   return 0
end
