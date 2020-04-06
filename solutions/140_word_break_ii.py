'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

# recursion with memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        word_dict = set(wordDict)
        return self.recurse(s, word_dict, 0, memo)

    def recurse(self, s, word_dict, start, memo):
        if start in memo:
            return memo[start]
        res = []
        if start == len(s):
            res.append("")
        for end in range(start + 1, len(s)+1):
            if s[start:end] in word_dict:
                cur_res = self.recurse(s, word_dict, end, memo)
                for item in cur_res:
                    if item == "":
                        res.append(s[start:end])
                    else:
                        res.append(f"{s[start:end]} {item}")
        memo[start] = res

        return res

# dp solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        
        valid = [False] * (len(s) + 1)
        valid[0] = True
        for end in range(1, len(s) + 1):
            for start in range(end):
                if valid[start] and s[start:end] in wordDict:
                    valid[end] = True
                    break
                    
        if not valid[-1]:
            return []
        
        dp = [None] * (len(s) +1)
        dp[0] = [""]
        for end in range(1, len(s) + 1):
            sentences = []
            for start in range(end):
                if len(dp[start]) > 0 and s[start:end] in wordDict:
                    for sentence in dp[start]:
                        if sentence == "":
                            sentences.append(s[start:end])
                        else:
                            sentences.append(f"{sentence} {s[start:end]}")
            dp[end] = sentences
        print(valid)
        print(dp)
        return dp[len(s)]