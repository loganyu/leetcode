'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        all_combo_dict = defaultdict(set)
        l = len(beginWord)
        for word in wordList:
            for i in range(0, l):
                generic_word = f"{word[:i]}*{word[i+1:]}"
                all_combo_dict[generic_word].add(word)
        
        queue = deque([[beginWord]])
        paths = []
        visited = {}
        path_found = False
        while queue:
            new_visited = {}
            for _ in range(len(queue)):
                path = queue.popleft()
                current_word = path[-1]
                neighbors = self.get_neighbors(current_word, all_combo_dict)
                for word in neighbors:
                    if word == endWord:
                        paths.append(path + [word])
                        path_found = True
                    elif word not in visited:
                        new_visited[word] = True
                        queue.append(path + [word])
            if path_found:
                break
            visited.update(new_visited)
        
        return paths
    
    def get_neighbors(self, current_word, all_combo_dict):
        l = len(current_word)
        neighbors = []
        for i in range(0,l):
            intermediate_word = f"{current_word[:i]}*{current_word[i+1:]}"
            if intermediate_word in all_combo_dict:
                neighbors.extend(all_combo_dict[intermediate_word])
        
        return neighbors

