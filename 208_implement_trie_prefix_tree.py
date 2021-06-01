'''
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
'''

from collections import defaultdict

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.links[char]
        node.is_word = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find_node(word)
        if node:
            return node.is_word
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find_node(prefix)
        if node:
            return True
        return False
    
    def find_node(self, word):
        node = self.root
        for char in word:
            if char not in node.links:
                return False
            node = node.links[char]
            
        return node 

class Node:
    
    def __init__(self):
        self.links = defaultdict(Node)
        self.is_word = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

