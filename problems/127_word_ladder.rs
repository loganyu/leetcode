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

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        let mut hm: HashMap<String, Vec<String>> = HashMap::new();
        for word in word_list.iter() {
            for i in 0..word.len() {
                let s = word.as_str();
                let key = (&s[0..i]).to_string() + "*" + &s[i + 1..];
                if let Some(v) = hm.get_mut(&key) {
                    v.push(s.to_string());
                } else {
                    hm.insert(key, vec![s.to_string()]);
                }
            }
        }
        
        let mut hs: HashSet<String> = HashSet::new();
        let mut vq: VecDeque<(String, i32)> = VecDeque::new();
        hs.insert(begin_word.to_string());
        vq.push_back((begin_word, 1));
        while let Some(front) = vq.pop_front() {
            let s = front.0.as_str();
            for i in 0..s.len() {
                let key = (&s[0..i]).to_string() + "*" + &s[i + 1..];
                if let Some(v) = hm.get(&key) {
                    for next in v.iter() {
                        if *next == end_word {
                            return front.1 + 1;
                        }
                        if !hs.contains(next) {
                            hs.insert(next.to_string());
                            vq.push_back((next.to_string(), front.1 + 1));
                        }
                    }
                }
            }
        }
        
        0
    }
}

