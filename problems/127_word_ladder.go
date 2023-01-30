/*
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
*/

type node struct {
    word string
    state int
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
    l := len(beginWord)
    dict := make(map[string][]string)
    for i := 0; i < len(wordList); i++ {
        for j:= 0; j < l; j++ {
            generic_word := wordList[i][:j] + "*" + wordList[i][j+1:]
            dict[generic_word] = append(dict[generic_word], wordList[i])
        }
    }
    
    queue := []node{node{word: beginWord, state: 1}}
    set := make(map[string]struct{})
    set[beginWord] = struct{}{}
    
    for len(queue) != 0 {
        current_node := queue[0]
        queue = queue[1:]
        for i := 0; i < l; i++ {
            intermediate_word := current_node.word[:i] + "*" + current_node.word[i+1:]
            for j := 0; j < len(dict[intermediate_word]); j++ {
                if dict[intermediate_word][j] == endWord {
                    return current_node.state + 1
                }
                if _, ok := set[dict[intermediate_word][j]]; !ok {
                    
                    set[dict[intermediate_word][j]] = struct{}{}
                    queue = append(queue, node{word: dict[intermediate_word][j], state: current_node.state + 1})
                }
            }
        }
    }
    return 0;
}

