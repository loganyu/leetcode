'''
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
'''

from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(word, 0, self.root)
    
    def match(self, word, i, node):
        if i == len(word):
            return node.is_word
        if word[i] != '.':
            child_node = node.children.get(word[i])
            if child_node:
                return self.match(word, i+1, child_node)
            else:
                return False
        else:
            for child_node in node.children.values():
                if self.match(word, i+1, child_node):
                    return True
            return False
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
