'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        back_idx = 0
        max_count = 0
        
        for i in range(len(s)):
            letter = s[i]
            if letter in seen and seen[letter] >= back_idx:
                current_count = i - back_idx
                max_count = max(max_count, current_count)
                back_idx = seen[letter] + 1
            seen[letter] = i
        current_count = len(s) - back_idx
        
        return max(max_count, current_count)
            
                
        
