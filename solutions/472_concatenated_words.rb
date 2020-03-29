=begin
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
=end

# @param {String[]} words
# @return {String[]}
def find_all_concatenated_words_in_a_dict(words)
    words.sort_by!{|word| word.length}
    word_dict = Set.new
    result = []
    words.each do |word|
        if can_form(word, word_dict)
            result << word
        end
        word_dict.add(word)
    end
    
    return result
end

def can_form(word, word_dict)
    if word_dict.include?(word)
        return true
    end
    (1...word.length).each do |i|
        if word_dict.include?(word[0...i]) && can_form(word[i..-1], word_dict)
            return true
        end
    end
    
    return false
end

