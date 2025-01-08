'''
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string



Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.
'''

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []

        for current_word_index in range(len(words)):
            lps = self._compute_lps_array(words[current_word_index])
            for other_word_index in range(len(words)):
                if current_word_index == other_word_index:
                    continue

                if self._is_substring_of(
                    words[current_word_index], words[other_word_index], lps
                ):
                    matching_words.append(words[current_word_index])
                    break

        return matching_words

    def _compute_lps_array(self, sub: str) -> List[int]:
        lps = [0] * len(sub)
        current_index = 1
        length = 0

        while current_index < len(sub):
            if sub[current_index] == sub[length]:
                length += 1
                lps[current_index] = length
                current_index += 1
            else:
                if length > 0:
                    length = lps[
                        length - 1
                    ]
                else:
                    current_index += 1
        return lps

    def _is_substring_of(self, sub: str, main: str, lps) -> bool:
        main_index = 0
        sub_index = 0

        while main_index < len(main):
            if main[main_index] == sub[sub_index]:
                main_index += 1
                sub_index += 1
                if sub_index == len(sub):
                    return True
            else:
                if sub_index > 0:
                    sub_index = lps[sub_index - 1]
                else:
                    main_index += 1
        return False

