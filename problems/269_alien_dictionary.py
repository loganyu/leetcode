'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''

from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        wordGraph = defaultdict(set)
        n = len(words)
        degrees = {}

        for word in words:
            for char in word:
                degrees[char] = 0

        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            if word1 == word2:
                continue
            if word1.startswith(word2):
                return ""
            wordLength = len(word1)
            for j in range(wordLength):
                if word1[j] != word2[j]:
                    if word2[j] not in wordGraph[word1[j]]:
                        wordGraph[word1[j]].add(word2[j])
                        degrees[word2[j]] += 1
                    break

        sol = ""
        queue = deque()
        for letter, numDegrees in degrees.items():
            if numDegrees == 0:
                queue.append(letter)

        while len(queue) > 0:
            char = queue.popleft()
            sol += char
            if char in wordGraph:
                for nextChar in wordGraph[char]:
                    degrees[nextChar] -= 1
                    if degrees[nextChar] == 0:
                        queue.append(nextChar)

        if len(sol) != len(degrees):
            return ""

        return sol
        