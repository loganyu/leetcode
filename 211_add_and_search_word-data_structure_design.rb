=begin
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
=end

class WordDictionary

=begin
    Initialize your data structure here.
=end
    def initialize()
        @root = TrieNode.new
    end

=begin
    Adds a word into the data structure.
    :type word: String
    :rtype: Void
=end
    def add_word(word)
        node = @root
        word.each_char do |char|
            letter_index = char.ord - 'a'.ord
            node.children[letter_index] ||= TrieNode.new
            node = node.children[letter_index]
        end
        node.is_word = true
    end


=begin
    Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
    :type word: String
    :rtype: Boolean
=end
    def search(word)
        match(word, 0, @root)
    end
    
    private
    
    def match(word, i, node)
        if i == word.length
            return node.is_word
        end
        if word[i] != '.'
            letter_index = word[i].ord - 'a'.ord
            child_node = node.children[letter_index]
            if child_node
                match(word, i+1, child_node)
            else
                return false
            end
        else
            (0...node.children.length).each do |letter_index|
                child_node = node.children[letter_index]
                if child_node
                    if match(word, i+1, child_node)
                        return true
                    end
                end
            end
            
            return false
        end
    end
end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary.new()
# obj.add_word(word)
# param_2 = obj.search(word)

class TrieNode
    attr_accessor :children, :is_word
    def initialize
        @children = Array.new(26)
        @is_word = false
    end
end
