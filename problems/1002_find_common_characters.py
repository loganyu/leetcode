'''
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        result = []
        common_character_counts = collections.Counter(words[0])
        for i in range(1, words_size):
            current_character_counts = collections.Counter(words[i])
            for letter in common_character_counts.keys():
                common_character_counts[letter] = min(
                    common_character_counts[letter],
                    current_character_counts[letter],
                )
        for letter, count in common_character_counts.items():
            for _ in range(count):
                result.append(letter)

        return result


