=begin
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
=end

# @param {String[]} words
# @param {String} order
# @return {Boolean}
def is_alien_sorted(words, order)
    order_index = {}
    order.each_char.with_index do |char, i|
        order_index[char] = i
    end
    
    0.upto(words.length - 2).each do |i|
        word1 = words[i]
        word2 = words[i+1]
        in_order = false
        0.upto([word1.length - 1, word2.length - 1].min) do |j|
           if word1[j] != word2[j]
               if order_index[word1[j]] > order_index[word2[j]]
                   return false
               end
               
               in_order = true
               break
           end
        end
        
        if in_order
            next
        elsif word1.length > word2.length
            return false
        end
    end
       
    return true
end
