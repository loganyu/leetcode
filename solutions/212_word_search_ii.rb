=begin
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
=end

# @param {Character[][]} board
# @param {String[]} words
# @return {String[]}
def find_words(board, words)
    res = []
    root = build_trie(words)
    (0...board.length).each do |r|
        (0...board[0].length).each do |c|
            dfs(board, r, c, root, res)
        end
    end
    
    return res
end

def dfs(board, r, c, node, res)
    char = board[r][c]
    i = char.ord - 'a'.ord
    if char == '#' || node.next[i].nil?
        return
    end
    node = node.next[i]
    if node.word
        res << node.word
        node.word = nil
    end
    
    board[r][c] = '#'
    dfs(board, r+1, c, node, res) if r+1 < board.length
    dfs(board, r-1, c, node, res) if r-1 >= 0
    dfs(board, r, c+1, node, res) if c+1 < board[0].length
    dfs(board, r, c-1, node, res) if c-1 >= 0
    board[r][c] = char
end

class TrieNode
    attr_accessor :next, :word
    def initialize
        @next = Array.new(26)
        @word = nil
    end
end

def build_trie(words)
    root = TrieNode.new
    words.each do |word|
        curr = root
        word.each_char do |char|
            i = char.ord - 'a'.ord
            curr.next[i] ||= TrieNode.new
            curr = curr.next[i]
        end
        curr.word = word
    end
    
    return root
end

