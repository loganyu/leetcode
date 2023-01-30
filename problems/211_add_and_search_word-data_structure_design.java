/*
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
*/

class WordDictionary {
    Trie trie;

    public WordDictionary() {
        this.trie = new Trie();
    }
    
    public void addWord(String word) {
        trie.add(word);
    }
    
    public boolean search(String word) {
        return trie.search(word);
    }
}

class Trie {
    Trie[] children;
    boolean isWord;
    Trie(){ this.children = new Trie[26];}
    
    
    public void add(String word) {
        Trie curr = this;
        for(char c : word.toCharArray()){
            if(curr.children[c - 'a'] == null) curr.children[c - 'a'] = new Trie();
            curr = curr.children[c - 'a'];
        }
        curr.isWord = true;
    }
    
    public boolean search(String word) {
        return search(this, word, 0);
    }
    
    private boolean search(Trie curr, String word, int idx) {
        if (idx == word.length()) {
            return curr.isWord;
        }
        char c = word.charAt(idx);
        
        if (c != '.') {
            return curr.children[c - 'a'] != null && search(curr.children[c-'a'], word, idx+1);
        }
        
        for (int i = 0; i < 26; i++) {
            if (curr.children[i] != null) {
                if (search(curr.children[i], word, idx + 1)) {
                    return true;
                }
            }
        }
        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */

