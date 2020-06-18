'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(set)
        l = len(beginWord)
        for word in wordList:
            for i in range(l):
                generic_word = f"{word[:i]}*{word[i+1:]}"
                graph[generic_word].add(word)
        queue = deque([[beginWord, 1]])
        visited = set([beginWord])
        while queue:
            current_word, level = queue.popleft()
            for i in range(l):
                intermediate_word = f"{current_word[:i]}*{current_word[i+1:]}"
                if intermediate_word in graph:
                    for word in graph[intermediate_word]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited.add(word)
                            queue.append([word, level + 1])
                    del graph[intermediate_word]
        
        return 0
        
