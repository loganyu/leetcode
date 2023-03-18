/*
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
*/

use std::mem;
use std::boxed::Box;

#[derive(Debug)]
struct TrieNode {
    c_byte: u8,
    is_word: bool,
    children: [Option<Box<TrieNode>>; 26],
}

impl TrieNode {
    fn new(c_byte: u8) -> Self {
        TrieNode {
            c_byte,
            is_word: false,
            children: Default::default(),
        }
    }
}

#[derive(Debug)]
struct Trie {
    head: TrieNode,
}

impl Trie {

    fn new() -> Self {
        Trie {
            head: TrieNode::new(b'\0'),
        }
    }
    
    /** Inserts a word into the trie. */
    fn insert(&mut self, word: String) {
        let mut curr: &mut TrieNode = &mut self.head;
        for b in word.bytes() {
            let e_byte = Self::e_byte(b);
            let node = TrieNode::new(e_byte);
            curr = curr.children[e_byte as usize].get_or_insert(Box::new(node));
        }
        curr.is_word = true;
    }
    
    /** Returns if the word is in the trie. */
    fn search(&self, word: String) -> bool {
        match self.search_node(word) {
            Some(node) => node.is_word,
            None => false,
        }
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    fn starts_with(&self, prefix: String) -> bool {
        self.search_node(prefix).is_some()
    }
    
    fn search_node(&self, prefix: String) -> Option<&TrieNode> {
        let mut curr: &TrieNode = &self.head;
        for b in prefix.bytes() {
            let e_byte = Self::e_byte(b);
            match &curr.children[e_byte as usize] {
                Some(node) => curr = node,
                None => {
                    return None
                },
            }
        }
        
        Some(curr)
    }
    
    fn e_byte(b: u8) -> u8 {
        return b - b'a';
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */

