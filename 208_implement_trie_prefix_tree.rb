=begin
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
=end

class Trie

=begin
    Initialize your data structure here.
=end
    def initialize()
        @root = TrieNode.new
    end


=begin
    Inserts a word into the trie.
    :type word: String
    :rtype: Void
=end
    def insert(word)
        node = @root
        word.each_char do |char|
            node.links[char] ||= TrieNode.new
            node = node.links[char]
        end
        node.is_word = true
    end


=begin
    Returns if the word is in the trie.
    :type word: String
    :rtype: Boolean
=end
    def search(word)
        node = find_node(word)
        if node
            return node.is_word
        else
            return false
        end
    end


=begin
    Returns if there is any word in the trie that starts with the given prefix.
    :type prefix: String
    :rtype: Boolean
=end
    def starts_with(prefix)
        node = find_node(prefix)
        
        if node
            return true
        else
            return false
        end
    end
    
    private
    
    def find_node(word)
        node = @root
        word.each_char do |char|
            if node.links[char].nil?
                return nil
            end
            node = node.links[char]
        end
        
        return node
    end


end

class TrieNode
    attr_accessor :is_word, :links
        
    def initialize
        @links = {}
        @is_word = false
    end
end

# Your Trie object will be instantiated and called as such:
# obj = Trie.new()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)

