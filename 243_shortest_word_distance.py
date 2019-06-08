'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        min_distance = len(words)
        curr_word, idx = None, 0
        for i in range(len(words)):
            word = words[i]
            if word not in (word1, word2):
                continue
            if curr_word and word != curr_word:
                min_distance = min(min_distance, i - idx)
            curr_word, idx = word, i
        
        return min_distance
 
