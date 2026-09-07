'''
Given an array of keywords words and a string s, make all appearances of all keywords words[i] in s bold. Any letters between <b> and </b> tags become bold.

Return s after adding the bold tags. The returned string should use the least number of tags possible, and the tags should form a valid combination.



Example 1:

Input: words = ["ab","bc"], s = "aabcd"
Output: "a<b>abc</b>d"
Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.
Example 2:

Input: words = ["ab","cb"], s = "aabcd"
Output: "a<b>ab</b>cd"


Constraints:

1 <= s.length <= 500
0 <= words.length <= 50
1 <= words[i].length <= 10
s and words[i] consist of lowercase English letters.


Note: This question is the same as 616. Add Bold Tag in String.
'''

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        n = len(s)
        is_bold = [False] * n

        for word in words:
            w_len = len(word)
            start = s.find(word)
            while start != -1:
                for i in range(start, start + w_len):
                    is_bold[i] = True
                start = s.find(word, start + 1)

        result = []
        i = 0
        while i < n:
            if is_bold[i]:
                result.append("<b>")
                while i < n and is_bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1

        return "".join(result)
