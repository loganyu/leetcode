'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [None]*n
        word_dict = set(wordDict)
        return self.r_word_break(0, s, memo, word_dict, n)
    
    def r_word_break(self, start_idx, s, memo, word_dict, n):
        if start_idx == n:
            return True
        if memo[start_idx] != None:
            return memo[start_idx]
        
        for i in range(start_idx + 1, n+1):
            if s[start_idx:i] in word_dict and self.r_word_break(i, s, memo, word_dict, n):
                memo[start_idx] = True
                return True
        
        memo[start_idx] = False
        return False
                
# DP solution
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_dict:
                    dp[i] = True
                    break
        return dp[n]
