'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(start_ind, end_ind):
            while start_ind <= end_ind:
                if s[start_ind] != s[end_ind]:
                    return False
                start_ind += 1
                end_ind -= 1
            return True
        
        def dfs(start_ind, path):
            if start_ind >= len(s):
                self.res.append(path)
            
            for l in range(len(s) - start_ind):
                if isPalindrome(start_ind, start_ind + l):
                    dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]])
        self.res = []
        dfs(0,[])
        
        return self.res
        
