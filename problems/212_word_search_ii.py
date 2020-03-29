'''
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
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self):
        self.next = [None]*26
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = set()
        root = self.build_trie(words)
        n = len(board)
        m = len(board[0])
        for r in range(n):
            for c in range(m):
                self.traverse(r,c,n,m,board,root,output)
        
        return list(output)
    
    def traverse(self, r, c, n, m, board, node, output):
        char = board[r][c]
        i = ord(char) - ord('a')
        if not node.next[i]:
            return
        node = node.next[i]
        if node.word:
            output.add(node.word)
            node.word = None
        
        board[r][c] = None
        for dr, dc in [(1,0),(-1,0),(0,-1),(0,1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != None:
                self.traverse(nr,nc,n,m,board,node,output)
        board[r][c] = char
        
    def build_trie(self, words):
        root = TreeNode()
        for word in words:
            curr = root
            for char in word:
                i = ord(char) - ord('a')
                if not curr.next[i]:
                    curr.next[i] = TreeNode()
                curr = curr.next[i]
            curr.word = word
        
        return root

